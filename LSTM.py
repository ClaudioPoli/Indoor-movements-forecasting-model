from random import randint
from numpy import array
from numpy import argmax
from numpy import array_equal
from keras.utils import to_categorical
from keras.models import Model
from keras.layers import Input
from keras.layers import LSTM
from keras.layers import Dense
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from Main.MatMap import mat2,mat3,mat4,mat5,mat6
from Main.main import dff

import warnings
warnings.filterwarnings("ignore")


#FUNCTIONS

"""Funzione che genera liste di numeri comprese in un range definito da @lenght"""
def generate_sequence(length, n_unique):
	return [randint(1, n_unique-1) for _ in range(length)]

"""Funzione che genera uno specifico numero di sequenze da utilizzare 
per allenare il modello. La sequenza verrà prima di tutto generata chiamando
la funzione @generate_sequence(), poi si identificherà la parte della 
sequenza che fungerà da target per la predizione. Infine si effettuerà
l'encoding della sequenza originale, della sequenza target e della sequenza
shiftata."""
def get_dataset(n_in, n_out, cardinality, n_samples):
        X1, X2, y = list(), list(), list()
        for _ in range(n_samples):
                #Generating source sequence
                source = generate_sequence(n_in, cardinality) 
                #Defining padded target sequence
                target = source[-n_out:]
                #Creating padded input target sequence
                target_in = [0] + target[:-1]
                #Encoding
                src_encoded = to_categorical([source], num_classes=cardinality)
                tar_encoded = to_categorical([target], num_classes=cardinality)
                tar2_encoded = to_categorical([target_in], num_classes=cardinality)
                #Storing
                X1.append(src_encoded)
                X2.append(tar2_encoded)
                y.append(tar_encoded)
        X1 = np.squeeze(array(X1), axis=1) 
        X2 = np.squeeze(array(X2), axis=1) 
        y = np.squeeze(array(y), axis=1) 
        return X1, X2, y

"""Funzione che consente di definire una rete neurale di tipo encoder-decoder
In input ha tre argomenti:
@n_input: cardinalità della sequenza di input
@n_output: cardinalità della sequenza di output
@n_units: numero di celle da creare nei modelli encoder e decoder

Restituisce in output:
@model: modello da allenare mediante @source e @target
@encoder_model: modello encoder usato per effettuare predizioni su nuovi dati
@decoder_model: modello decoder usato per effettuare predizioni su nuovi dati"""
def define_models(n_input, n_output, n_units):
	#Defining training encoder
	encoder_inputs = Input(shape=(None, n_input))
	encoder = LSTM(n_units, return_state=True)
	encoder_outputs, state_h, state_c = encoder(encoder_inputs)
	encoder_states = [state_h, state_c]
	#Defining training decoder
	decoder_inputs = Input(shape=(None, n_output))
	decoder_lstm = LSTM(n_units, return_sequences=True, return_state=True)
	decoder_outputs, _, _ = decoder_lstm(decoder_inputs, initial_state=encoder_states)
	decoder_dense = Dense(n_output, activation='softmax')
	decoder_outputs = decoder_dense(decoder_outputs)
	model = Model([encoder_inputs, decoder_inputs], decoder_outputs)
	#Defining inference encoder
	encoder_model = Model(encoder_inputs, encoder_states)
	#Defining inference decoder
	decoder_state_input_h = Input(shape=(n_units,))
	decoder_state_input_c = Input(shape=(n_units,))
	decoder_states_inputs = [decoder_state_input_h, decoder_state_input_c]
	decoder_outputs, state_h, state_c = decoder_lstm(decoder_inputs, initial_state=decoder_states_inputs)
	decoder_states = [state_h, state_c]
	decoder_outputs = decoder_dense(decoder_outputs)
	decoder_model = Model([decoder_inputs] + decoder_states_inputs, [decoder_outputs] + decoder_states)
	#Return all models
	return model, encoder_model, decoder_model

"""Funzione che consente, dopo che è stato effettuato il training sul
modello, di generare una sequenza target sulla base della sequenza data
@infenc: modello encoder usato nella predizione di una nuova sequenza
@infdec: modello decoder usato nella predizione di una nuova sequenza
@source: sequenza iniziale codificata
@n_steps: numero di step nella sequenza target
@cardinality: cardinalità della sequenza in uscita"""
def predict_sequence(infenc, infdec, source, n_steps, cardinality):
	#Encodinf
	state = infenc.predict(source)
	#Start of sequence input
	target_seq = array([0.0 for _ in range(cardinality)]).reshape(1, 1, cardinality)
	#Collecting predictions
	output = list()
	for t in range(n_steps):
		#Predicting next item
		yhat, h, c = infdec.predict([target_seq] + state)
		#Storing prediction
		output.append(yhat[0,0,:])
		#Updating state
		state = [h, c]
		#Updating target sequence
		target_seq = yhat
	return array(output)

"""Funzione che permette di effettuare il decoding di una sequenza codificata"""
def one_hot_decode(encoded_seq):
	return [argmax(vector) for vector in encoded_seq]



#MAIN
nrows=0
df=dff
grid=df['Area'].max()
if(grid==4):
    nrows=2
elif(grid==9):
    nrows=3
elif(grid==16):
    nrows=4
elif(grid==25):
    nrows=5
elif(grid==36):
    nrows=6
    

#Model Configuration
n_features = (nrows*nrows) + 1
n_steps_in = 30
n_steps_out =15
n_cells=128
n_epochs=10
datasetLen=1000
ncols=nrows

#Model definition and compilation of the training model
train, infenc, infdec = define_models(n_features, n_features, n_cells)
train.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

#Generation of the training dataset
X1, X2, y = get_dataset(n_steps_in, n_steps_out, n_features, datasetLen)
print(X1.shape,X2.shape,y.shape)

#Model training
history = train.fit([X1, X2],y, epochs=n_epochs,batch_size=16,verbose=1)

# Plot training & validation accuracy values
plt.plot(history.history['acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.show()

#LSTM evaluation
total, correct = 100, 0
for _ in range(total):
	X1, X2, y = get_dataset(n_steps_in, n_steps_out, n_features, 1)
	target = predict_sequence(infenc, infdec, X1, n_steps_out, n_features)
	if array_equal(one_hot_decode(y[0]), one_hot_decode(target)):
		correct+=1
	elif np.allclose(one_hot_decode(y[0]), one_hot_decode(target),0,1):
		correct += 0.75
	elif np.allclose(one_hot_decode(y[0]), one_hot_decode(target),0,2):
		correct += 0.50
	elif np.allclose(one_hot_decode(y[0]), one_hot_decode(target),0,3):
		correct += 0.25
print('Accuracy: %.2f%%' % (float(correct)/float(total)*100.0))

#Examples
for _ in range(10):
	X1, X2, y = get_dataset(n_steps_in, n_steps_out, n_features, 1)
	target = predict_sequence(infenc, infdec, X1, n_steps_out, n_features)
	print('X=%s         y=%s,           Predicted=%s' % (one_hot_decode(X1[0]), one_hot_decode(y[0]), one_hot_decode(target)))


#Visualization
    
cmap = ListedColormap([ 'w', 'g','b'])

vect=list(range(n_steps_out))
plt.plot(vect,one_hot_decode(y[0]),color='green')
plt.plot(vect,one_hot_decode(target),color='blue')
plt.title("Green(original)    Blue(Predicted)")
plt.show()


for i in range (len(one_hot_decode(y[0]))):
        print("Step ",i+1)
        if (nrows==2):
            plt.matshow(mat2([2,2],one_hot_decode(y[0])[i],one_hot_decode(target)[i]),cmap=cmap)
        elif (nrows==3):
            plt.matshow(mat3([3,3],one_hot_decode(y[0])[i],one_hot_decode(target)[i]),cmap=cmap)
        elif (nrows==4):
            plt.matshow(mat4([4,4],one_hot_decode(y[0])[i],one_hot_decode(target)[i]),cmap=cmap)
        elif (nrows==5):
            plt.matshow(mat5([5,5],one_hot_decode(y[0])[i],one_hot_decode(target)[i]),cmap=cmap)
        elif (nrows==6):
            plt.matshow(mat6([6,6],one_hot_decode(y[0])[i],one_hot_decode(target)[i]),cmap=cmap)
        plt.xticks([])
        plt.yticks([])
        plt.show()
   
        
    
        
