import keras
from keras.layers import * # Conv2D,Input,Lambda,Dropout, MaxPooling2D, Conv2DTranspose
from keras.models import *
from keras.initializers import *


def dmcnn(img_rows, img_cols, img_channels = 3):
    input = Input((img_rows, img_cols, img_channels))

    x = Conv2D(128,(9,9),kernel_initializer = 'he_normal', activation='relu', padding='same')(input)
    x = Conv2D(64,(1,1),kernel_initializer = 'he_normal', activation='relu', padding='same')(x)
    y = Conv2D(3,(5,5),kernel_initializer = 'he_normal', activation='relu', padding='same')(x)

    model = Model(inputs = input, outputs = y)

    model.summary()

    return model


def dmcnnvd(img_rows, img_cols, img_channels):
    input = Input(img_rows, img_cols, img_channels)

    b = Conv2D(3, (5,5), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='relu', padding='same')(input)

    l0 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(input)
    l0 = BatchNormalization()(l0)
    l0 = Activation('selu')(l0)

    l1 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l0)
    l1 = BatchNormalization()(l1)
    l1 = Activation('selu')(l1)

    l2 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l1)
    l2 = BatchNormalization()(l2)
    l2 = Activation('selu')(l2)

    l3 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l2)
    l3 = BatchNormalization()(l3)
    l3 = Activation('selu')(l3)

    l4 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l3)
    l4 = BatchNormalization()(l4)
    l4 = Activation('selu')(l4)

    l5 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l4)
    l5 = BatchNormalization()(l5)
    l5 = Activation('selu')(l5)

    l6 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l5)
    l6 = BatchNormalization()(l6)
    l6 = Activation('selu')(l6)

    l7 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l6)
    l7 = BatchNormalization()(l7)
    l7 = Activation('selu')(l7)

    l8 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l7)
    l8 = BatchNormalization()(l8)
    l8 = Activation('selu')(l8)

    l9 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l8)
    l9 = BatchNormalization()(l9)
    l9 = Activation('selu')(l9)

    l10 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l9)
    l10 = BatchNormalization()(l10)
    l10 = Activation('selu')(l10)

    l11 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l10)
    l11 = BatchNormalization()(l11)
    l11 = Activation('selu')(l11)

    l12 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l11)
    l12 = BatchNormalization()(l12)
    l12 = Activation('selu')(l12)

    l13 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l12)
    l13 = BatchNormalization()(l13)
    l13 = Activation('selu')(l13)

    l14 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l13)
    l14 = BatchNormalization()(l14)
    l14 = Activation('selu')(l14)

    l15 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l14)
    l15 = BatchNormalization()(l15)
    l15 = Activation('selu')(l15)

    l16 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l15)
    l16 = BatchNormalization()(l16)
    l16 = Activation('selu')(l16)

    l17 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l16)
    l17 = BatchNormalization()(l17)
    l17 = Activation('selu')(l17)

    l18 = Conv2D(64, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l17)
    l18 = BatchNormalization()(l18)
    l18 = Activation('selu')(l18)

    l19 = Conv2D(3, (3,3), kernel_initializer = VarianceScaling(scale=2.0, mode='fan_in', distribution='normal'), activation='selu', padding='same')(l18)
    l19 = BatchNormalization()(l19)
    l19 = Activation('selu')(l19)

    y = Add()([l19, b])
    outputs = Activation('relu')(y)

    model = Model(inputs=[input], outputs=[outputs])
    model.summary()

    return model