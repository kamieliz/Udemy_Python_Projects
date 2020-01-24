from azureml.core import Model

model = Model.register(workspace=ws,
                       model_name='classification_model',
                       model_path='model.pkl', # local path
                       description='A classification model',
                       tags={'dept': 'sales'},
                       model_framework=Model.Framework.SCIKITLEARN,
                       model_framework_version='0.20.3')

# using run reference
run.register_model( model_name='classification_model',
                    model_path='outputs/model.pkl', # run outputs path
                    description='A classification model',
                    tags={'dept': 'sales'},
                    model_framework=Model.Framework.SCIKITLEARN,
                    model_framework_version='0.20.3')
					
#View in ML Studio
from azureml.core import Model

for model in Model.list(ws):
    # Get model name and auto-generated version
    print(model.name, 'version:', model.version) 										   