Vim�UnDo� -2�����s@�a���i���de�n���}ʵ�   .                                   _�{    _�                             ����                                                                                                                                                                                                                                                                                                                                                             _�z�     �               5�_�                    ,        ����                                                                                                                                                                                                                                                                                                                                                             _�{     �   +   ,       J   #print(df.shape)       6##################VISULAIZING UNIVARIATE DISTRIBUTIONS       0#visualizing correlations the different features   ##sns.heatmap(df.corr(), annot=True)   0#univariate distributions of continuous features   #sns.displot(df['bedrooms'])   #sns.displot(df['bathrooms'])   #sns.displot(df['sqft_living'])   #sns.displot(df['sqft_lot'])   #sns.displot(df['floors'])   #sns.displot(df['view'])   #sns.displot(df['condition'])   #sns.displot(df['sqft_above'])   !#sns.displot(df['sqft_basement'])       ,#visualizing univariate distro of the target   #sns.displot(df['price'])                   &#########################PREPROCESSING       #creating x and y vectors   $X = df.drop('price', axis='columns')   y = df.price       $col_trans = make_column_transformer(   V    (SimpleImputer(missing_values=0.0, strategy='median'), ['bedrooms', 'bathrooms']),   V    (SimpleImputer(missing_values=0, strategy='median'), ['sqft_lot', 'sqft_living']),        (OneHotEncoder(), ['city']),       remainder='passthrough'   )           *X_transformed = col_trans.fit_transform(X)   Dx_train, x_test, y_train, y_test = train_test_split(X_transformed,y)   #print(x_train.shape)   #print(x_test.shape)   #print(y_train.shape)   #print(y_test.shape)           #########non-scaled   linreg = LinearRegression()   )cross_val_score(linreg, x_train, y_train)       linreg.fit(x_train, y_train)   Gprint("Test set accuracy: {:.2f}".format(linreg.score(x_test, y_test)))                   #########scaled       $col_trans = make_column_transformer(   V    (SimpleImputer(missing_values=0.0, strategy='median'), ['bedrooms', 'bathrooms']),   V    (SimpleImputer(missing_values=0, strategy='median'), ['sqft_lot', 'sqft_living']),       (StandardScaler(), [cols])        (OneHotEncoder(), ['city']),       remainder='passthrough'   )           *X_transformed = col_trans.fit_transform(X)   Dx_train, x_test, y_train, y_test = train_test_split(X_transformed,y)       :pipe = make_pipeline(StandardScaler(), LinearRegression())   'cross_val_score(pipe, x_train, y_train)       pipe.fit(x_train, y_train)   Lprint("Scaled test set accuracy: {:.2f}".format(pipe.score(x_test, y_test)))5�_�                     +        ����                                                                                                                                                                                                                                                                                                                                                             _�{    �   +               �   +            5��