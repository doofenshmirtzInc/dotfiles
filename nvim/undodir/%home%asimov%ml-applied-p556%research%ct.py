Vim�UnDo� d�јO�d���p�>�	���3�r�n   L       remainder=passthrough   H                          _�</    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�:�     �      
   B    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�:�     �      
   C    �      	   C    5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             _�:�    �      
   D      3from sklearn.compose import make_column_transformer5�_�                    D        ����                                                                                                                                                                                                                                                                                                                                                             _�;}     �   D               �   D            5�_�                   F        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   F   H   H          �   F   H   G    �   E              Colum5�_�                    G       ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   F   H   H          transformers=('encoder')5�_�      	              G   4    ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   F   H   H      6    transformers=('encoder', OneHotEncoder(), ['Sex'])5�_�      
           	   G   B    ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   F   I   H      B    transformers=('encoder', OneHotEncoder(), ['Sex', 'Embarked'])5�_�   	              
   I        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   I               �   I            5�_�   
                 L        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   K              ct.fit_transform(X)5�_�                    D        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   C   E   L      $print(column_trans.fit_transform(X))5�_�                    >        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   =   ?   L      'column_trans = make_column_transformer(5�_�                    ?       ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   >   @   L      +    (OneHotEncoder(), ['Sex', 'Embarked']),5�_�                    @       ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   ?   A   L          remainder='passthrough'5�_�                    A        ����                                                                                                                                                                                                                                                                                                                                                             _�;�    �   @   B   L      )5�_�                     H       ����                                                                                                                                                                                                                                                                                                                                                             _�<.    �   G   I   L          remainder=passthrough5�_�                    F        ����                                                                                                                                                                                                                                                                                                                                                             _�;�     �   E   G          ct = ColumnTransformer(   )�   F   G   G          �   F   H   H          transformers=(5��