Vim�UnDo� vяLc�yM���X��DtP�J����_�"f�   8       print(hel)   8   
      J       J   J   J    _��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�UJ     �                   5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�UQ     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�UX     �                Ctest_names = pd.read_csv(data_path + 'test_names.csv', index_col=0)5�_�                            ����                                                                                                                                                                                                                                                                                                                                       /           V        _�U�     �                    print('shape of boys array:')   print(f'ndim: {X_boys.ndim}')   print(f'shape: {X_boys.shape}')               val = X_boys[0]   print(f'{val}:{type(val)}')   new_val = str(val[0])   #print(f'{new_val}:{type(new_val)}')   print(len(new_val))       #adding length col:   VX_boys = np.column_stack((X_boys, np.array([len(str(label[0])) for label in X_boys])))   print(X_boys)       print('shape of boys aray:')   print(f'ndim: {X_boys.ndim}')   print(f'shape: {X_boys.shape}')5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                  �               5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                 name = X_boys[0]5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                  �               5�_�      	                 	    ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                  �               5�_�      
           	          ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                  �               5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�     �                print5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                  V        _�U�    �                �             5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             _�V?     �                  �               5�_�                    "       ����                                                                                                                                                                                                                                                                                                                                                             _�VT     �   !              for i in range(len(X_boys))5�_�                    #   
    ����                                                                                                                                                                                                                                                                                                                                                             _�Vi     �   "                  print()5�_�                    #       ����                                                                                                                                                                                                                                                                                                                                                             _�Vo     �   "                  print(X_boys[i][0])5�_�                    $       ����                                                                                                                                                                                                                                                                                                                                                             _�V�     �   $                  �   $            5�_�                    "       ����                                                                                                                                                                                                                                                                                                                                                             _�V�     �   !   #   &       �   !   #   %    5�_�                    &       ����                                                                                                                                                                                                                                                                                                                                                             _�V�    �   &                  �   &            5�_�                    )       ����                                                                                                                                                                                                                                                                                                                                                             _�V�    �   )               �   )            5�_�                    *        ����                                                                                                                                                                                                                                                                                                                                                             _�W    �   *               �   *            5�_�                   &       ����                                                                                                                                                                                                                                                                                                                                                             _�Y     �   &   *   ,          �   &   (   +    5�_�                    )       ����                                                                                                                                                                                                                                                                                                                                                             _�Y     �   )   +   /       �   )   +   .    5�_�                    *       ����                                                                                                                                                                                                                                                                                                                                                             _�Y7     �   )   +   /      prefixes.append(item[-3:])5�_�                    *        ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   )   +   /      'prefixes.append(item[-3:] for item in )5�_�                    *       ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   )   ,   /      for i in range(len(X_boys))5�_�                    +   !    ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   *   ,   0      #    prefixes.append(str(X_boys[i]))5�_�                    +   %    ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   *   ,   0      &    prefixes.append(str(X_boys[i][0]))5�_�                    +   (    ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   +   .   1          �   +   -   0    5�_�                     -        ����                                                                                                                                                                                                                                                                                                                                                             _�Y�     �   ,   -          print(prefixes)5�_�      !               "        ����                                                                                                                                                                                                                                                                                                                            "           "           V        _�Y�     �   !   #   1      prefixes = []5�_�       "           !   #        ����                                                                                                                                                                                                                                                                                                                            "           "           V        _�Y�     �   "   $   1      for i in range(len(X_boys)):5�_�   !   #           "   $       ����                                                                                                                                                                                                                                                                                                                            "           "           V        _�Y�     �   #   %   1          print(X_boys[i][0])5�_�   "   $           #   %       ����                                                                                                                                                                                                                                                                                                                            "           "           V        _�Y�     �   $   &   1          prefix = input('prefix: ')5�_�   #   %           $   &       ����                                                                                                                                                                                                                                                                                                                            "           "           V        _�Y�    �   %   '   1          prefixes.append(prefix)5�_�   $   &           %           ����                                                                                                                                                                                                                                                                                                                                                             _�z�     �         2       �         1    5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                             _�z�    �         4       �         3    5�_�   &   (           '           ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �         4      X_boys = boy_names.values5�_�   '   )           (           ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �         4      X_girls = girl_names.values5�_�   (   *           )           ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �         4       5�_�   )   +           *           ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �          4      name = X_boys[0][0]5�_�   *   ,           +            ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �      !   4      print(name)5�_�   +   -           ,   !        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �       "   4      print(type(name))5�_�   ,   8           -   "        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   !   #   4      print(len(name))5�_�   -   9   .       8   ,        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{#     �   +   -   4      prefixes = []5�_�   8   :           9   -        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{$     �   ,   .   4      for i in range(len(X_boys)):5�_�   9   ;           :   .       ����                                                                                                                                                                                                                                                                                                                                                  V       _�{$     �   -   /   4      +    prefixes.append(str(X_boys[i][0])[-3:])5�_�   :   <           ;   2        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{&     �   1   3   4      print(prefixes)5�_�   ;   =           <   3        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{&     �   2   4   4      6X_boys = np.column_stack((X_boys, np.array(prefixes)))5�_�   <   >           =   4        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{&    �   3              print(X_boys)5�_�   =   ?           >           ����                                                                                                                                                                                                                                                                                                                                                             _�{�     �                print(boy_names.describe())5�_�   >   @           ?           ����                                                                                                                                                                                                                                                                                                                                                             _�{�     �         3    �         3    5�_�   ?   A           @          ����                                                                                                                                                                                                                                                                                                                                                             _�{�    �         4      print(boy_names.info())5�_�   @   B           A           ����                                                                                                                                                                                                                                                                                                                                                             _�{�     �         5       �         4    5�_�   A   C           B          ����                                                                                                                                                                                                                                                                                                                                                             _�{�     �         5    �         5    5�_�   B   D           C          ����                                                                                                                                                                                                                                                                                                                                                             _�{�     �         6      print(boy_names.describe())5�_�   C   F           D           ����                                                                                                                                                                                                                                                                                                                                                V       _�{�   
 �                print(boy_names.info())   print(girl_names.info())5�_�   D   G   E       F           ����                                                                                                                                                                                                                                                                                                                                                 v       _�|x     �         4      2data_path = '/home/asimov/ml-applied-p556/hw2/q1/'5�_�   F   H           G           ����                                                                                                                                                                                                                                                                                                                                                 v       _�|�    �                Cgirl_names = pd.read_csv(data_path + 'girl_names.csv', index_col=0)�                Aboy_names = pd.read_csv(data_path + 'boy_names.csv', index_col=0)�                2DATA_PATH = '/home/asimov/ml-applied-p556/hw2/q1/'5�_�   G   I           H   4        ����                                                                                                                                                                                                                                                                                                                                                             _��     �   4               �   4            5�_�   H   J           I   7       ����                                                                                                                                                                                                                                                                                                                                                             _��     �   6              def hello()5�_�   I               J   8   
    ����                                                                                                                                                                                                                                                                                                                                                             _��    �   7                  print(hel)5�_�   D           F   E           ����                                                                                                                                                                                                                                                                                                                                                             _�|r     �         4      *u = '/home/asimov/ml-applied-p556/hw2/q1/'5�_�   -   /       8   .   #        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   "   $   4      #5�_�   .   0           /   $        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   #   %   4      #5�_�   /   1           0   %        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   $   &   4      ##prefixes = []5�_�   0   2           1   &        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   %   '   4      ##for i in range(len(X_boys)):5�_�   1   3           2   '       ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   &   (   4          ##print(X_boys[i][0])5�_�   2   4           3   (       ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   '   )   4           ##prefix = input('prefix: ')5�_�   3   5           4   )       ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   (   *   4          ##prefixes.append(prefix)5�_�   4   6           5   *        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   )   +   4      #5�_�   5   7           6   +        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   *   ,   4      #5�_�   6               7   ,        ����                                                                                                                                                                                                                                                                                                                                                  V       _�{     �   +   -   4      #prefixes = []5�_�                   &       ����                                                                                                                                                                                                                                                                                                                                                             _�Y     �   &   '   +          �   &   (   ,          prefixes = [   ]�   (   )   .          �   (   *   /       �   '   *   /      prefixes = [5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             _�X�     �   $   &   +          prefix = kkjkjkjkjkjkjkj5��