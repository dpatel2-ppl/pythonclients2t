# swagger-client
Speech Services API v3.0.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v3.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen
For more information, please visit [https://docs.microsoft.com/azure/cognitive-services/speech-service/support](https://docs.microsoft.com/azure/cognitive-services/speech-service/support)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Ocp-Apim-Subscription-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Ocp-Apim-Subscription-Key'] = 'Bearer'
# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.CustomSpeechDatasetsForModelAdaptationApi(swagger_client.ApiClient(configuration))
dataset = swagger_client.Dataset() # Dataset | Definition for the new dataset.

try:
    # Uploads and creates a new dataset by getting the data from a specified URL.
    api_response = api_instance.create_dataset(dataset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->create_dataset: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CustomSpeechDatasetsForModelAdaptationApi* | [**create_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#create_dataset) | **POST** /datasets | Uploads and creates a new dataset by getting the data from a specified URL.
*CustomSpeechDatasetsForModelAdaptationApi* | [**delete_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#delete_dataset) | **DELETE** /datasets/{id} | Deletes the specified dataset.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset) | **GET** /datasets/{id} | Gets the dataset identified by the given ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_dataset_file**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset_file) | **GET** /datasets/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a dataset (identified with id).
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_dataset_files**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset_files) | **GET** /datasets/{id}/files | Gets the files of the dataset identified by the given ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_datasets) | **GET** /datasets | Gets a list of datasets for the authenticated subscription.
*CustomSpeechDatasetsForModelAdaptationApi* | [**get_supported_locales_for_datasets**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#get_supported_locales_for_datasets) | **GET** /datasets/locales | Gets a list of supported locales for datasets.
*CustomSpeechDatasetsForModelAdaptationApi* | [**update_dataset**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#update_dataset) | **PATCH** /datasets/{id} | Updates the mutable details of the dataset identified by its ID.
*CustomSpeechDatasetsForModelAdaptationApi* | [**upload_dataset_from_form**](docs/CustomSpeechDatasetsForModelAdaptationApi.md#upload_dataset_from_form) | **POST** /datasets/upload | Uploads data and creates a new dataset.
*CustomSpeechEndpointsApi* | [**create_endpoint**](docs/CustomSpeechEndpointsApi.md#create_endpoint) | **POST** /endpoints | Creates a new endpoint.
*CustomSpeechEndpointsApi* | [**delete_base_model_log**](docs/CustomSpeechEndpointsApi.md#delete_base_model_log) | **DELETE** /endpoints/base/{locale}/files/logs/{logId} | Deletes one audio or transcription log that have been stored when using the default base model of a given language.
*CustomSpeechEndpointsApi* | [**delete_base_model_logs**](docs/CustomSpeechEndpointsApi.md#delete_base_model_logs) | **DELETE** /endpoints/base/{locale}/files/logs | Deletes the specified audio and transcription logs that have been stored when using the default base model of a given language. It deletes all logs before (and including) a specific day.
*CustomSpeechEndpointsApi* | [**delete_endpoint**](docs/CustomSpeechEndpointsApi.md#delete_endpoint) | **DELETE** /endpoints/{id} | Deletes the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**delete_endpoint_log**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_log) | **DELETE** /endpoints/{id}/files/logs/{logId} | Deletes one audio or transcription log that have been stored for a given endpoint.
*CustomSpeechEndpointsApi* | [**delete_endpoint_logs**](docs/CustomSpeechEndpointsApi.md#delete_endpoint_logs) | **DELETE** /endpoints/{id}/files/logs | Deletes the specified audio and transcription logs that have been stored for a given endpoint. It deletes all logs before (and including) a specific day.
*CustomSpeechEndpointsApi* | [**get_base_model_log**](docs/CustomSpeechEndpointsApi.md#get_base_model_log) | **GET** /endpoints/base/{locale}/files/logs/{logId} | Gets a specific audio or transcription log for the default base model in a given language.
*CustomSpeechEndpointsApi* | [**get_base_model_logs**](docs/CustomSpeechEndpointsApi.md#get_base_model_logs) | **GET** /endpoints/base/{locale}/files/logs | Gets the list of audio and transcription logs that have been stored when using the default base model of a given language.
*CustomSpeechEndpointsApi* | [**get_endpoint**](docs/CustomSpeechEndpointsApi.md#get_endpoint) | **GET** /endpoints/{id} | Gets the endpoint identified by the given ID.
*CustomSpeechEndpointsApi* | [**get_endpoint_log**](docs/CustomSpeechEndpointsApi.md#get_endpoint_log) | **GET** /endpoints/{id}/files/logs/{logId} | Gets a specific audio or transcription log for a given endpoint.
*CustomSpeechEndpointsApi* | [**get_endpoint_logs**](docs/CustomSpeechEndpointsApi.md#get_endpoint_logs) | **GET** /endpoints/{id}/files/logs | Gets the list of audio and transcription logs that have been stored for a given endpoint.
*CustomSpeechEndpointsApi* | [**get_endpoints**](docs/CustomSpeechEndpointsApi.md#get_endpoints) | **GET** /endpoints | Gets the list of endpoints for the authenticated subscription.
*CustomSpeechEndpointsApi* | [**get_supported_locales_for_endpoints**](docs/CustomSpeechEndpointsApi.md#get_supported_locales_for_endpoints) | **GET** /endpoints/locales | Gets a list of supported locales for endpoint creations.
*CustomSpeechEndpointsApi* | [**update_endpoint**](docs/CustomSpeechEndpointsApi.md#update_endpoint) | **PATCH** /endpoints/{id} | Updates the metadata of the endpoint identified by the given ID.
*CustomSpeechModelEvaluationsApi* | [**create_evaluation**](docs/CustomSpeechModelEvaluationsApi.md#create_evaluation) | **POST** /evaluations | Creates a new evaluation.
*CustomSpeechModelEvaluationsApi* | [**delete_evaluation**](docs/CustomSpeechModelEvaluationsApi.md#delete_evaluation) | **DELETE** /evaluations/{id} | Deletes the evaluation identified by the given ID.
*CustomSpeechModelEvaluationsApi* | [**get_evaluation**](docs/CustomSpeechModelEvaluationsApi.md#get_evaluation) | **GET** /evaluations/{id} | Gets the evaluation identified by the given ID.
*CustomSpeechModelEvaluationsApi* | [**get_evaluation_file**](docs/CustomSpeechModelEvaluationsApi.md#get_evaluation_file) | **GET** /evaluations/{id}/files/{fileId} | Gets one specific file (identified with fileId) from an evaluation (identified with id).
*CustomSpeechModelEvaluationsApi* | [**get_evaluation_files**](docs/CustomSpeechModelEvaluationsApi.md#get_evaluation_files) | **GET** /evaluations/{id}/files | Gets the files of the evaluation identified by the given ID.
*CustomSpeechModelEvaluationsApi* | [**get_evaluations**](docs/CustomSpeechModelEvaluationsApi.md#get_evaluations) | **GET** /evaluations | Gets the list of evaluations for the authenticated subscription.
*CustomSpeechModelEvaluationsApi* | [**get_supported_locales_for_evaluations**](docs/CustomSpeechModelEvaluationsApi.md#get_supported_locales_for_evaluations) | **GET** /evaluations/locales | Gets a list of supported locales for evaluations.
*CustomSpeechModelEvaluationsApi* | [**update_evaluation**](docs/CustomSpeechModelEvaluationsApi.md#update_evaluation) | **PATCH** /evaluations/{id} | Updates the mutable details of the evaluation identified by its id.
*CustomSpeechModelsApi* | [**copy_model_to_subscription**](docs/CustomSpeechModelsApi.md#copy_model_to_subscription) | **POST** /models/{id}/copyto | Copies a model from one subscription to another.
*CustomSpeechModelsApi* | [**create_model**](docs/CustomSpeechModelsApi.md#create_model) | **POST** /models | Creates a new model.
*CustomSpeechModelsApi* | [**delete_model**](docs/CustomSpeechModelsApi.md#delete_model) | **DELETE** /models/{id} | Deletes the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_base_model**](docs/CustomSpeechModelsApi.md#get_base_model) | **GET** /models/base/{id} | Gets the base model identified by the given ID.
*CustomSpeechModelsApi* | [**get_base_model_manifest**](docs/CustomSpeechModelsApi.md#get_base_model_manifest) | **GET** /models/base/{id}/manifest | Returns an manifest for this base model which can be used in an on-premise container.
*CustomSpeechModelsApi* | [**get_base_models**](docs/CustomSpeechModelsApi.md#get_base_models) | **GET** /models/base | Gets the list of base models for the authenticated subscription.
*CustomSpeechModelsApi* | [**get_model**](docs/CustomSpeechModelsApi.md#get_model) | **GET** /models/{id} | Gets the model identified by the given ID.
*CustomSpeechModelsApi* | [**get_model_manifest**](docs/CustomSpeechModelsApi.md#get_model_manifest) | **GET** /models/{id}/manifest | Returns an manifest for this model which can be used in an on-premise container.
*CustomSpeechModelsApi* | [**get_models**](docs/CustomSpeechModelsApi.md#get_models) | **GET** /models | Gets the list of custom models for the authenticated subscription.
*CustomSpeechModelsApi* | [**get_supported_locales_for_models**](docs/CustomSpeechModelsApi.md#get_supported_locales_for_models) | **GET** /models/locales | Gets a list of supported locales for model adaptation.
*CustomSpeechModelsApi* | [**update_model**](docs/CustomSpeechModelsApi.md#update_model) | **PATCH** /models/{id} | Updates the metadata of the model identified by the given ID.
*CustomSpeechProjectsApi* | [**create_project**](docs/CustomSpeechProjectsApi.md#create_project) | **POST** /projects | Creates a new project.
*CustomSpeechProjectsApi* | [**delete_project**](docs/CustomSpeechProjectsApi.md#delete_project) | **DELETE** /projects/{id} | Deletes the project identified by the given ID.
*CustomSpeechProjectsApi* | [**get_datasets_for_project**](docs/CustomSpeechProjectsApi.md#get_datasets_for_project) | **GET** /projects/{id}/datasets | Gets the list of datasets for specified project.
*CustomSpeechProjectsApi* | [**get_endpoints_for_project**](docs/CustomSpeechProjectsApi.md#get_endpoints_for_project) | **GET** /projects/{id}/endpoints | Gets the list of endpoints for specified project.
*CustomSpeechProjectsApi* | [**get_evaluations_for_project**](docs/CustomSpeechProjectsApi.md#get_evaluations_for_project) | **GET** /projects/{id}/evaluations | Gets the list of evaluations for specified project.
*CustomSpeechProjectsApi* | [**get_models_for_project**](docs/CustomSpeechProjectsApi.md#get_models_for_project) | **GET** /projects/{id}/models | Gets the list of models for specified project.
*CustomSpeechProjectsApi* | [**get_project**](docs/CustomSpeechProjectsApi.md#get_project) | **GET** /projects/{id} | Gets the project identified by the given ID.
*CustomSpeechProjectsApi* | [**get_projects**](docs/CustomSpeechProjectsApi.md#get_projects) | **GET** /projects | Gets the list of projects for the authenticated subscription.
*CustomSpeechProjectsApi* | [**get_supported_project_locales**](docs/CustomSpeechProjectsApi.md#get_supported_project_locales) | **GET** /projects/locales | Gets the list of supported locales.
*CustomSpeechProjectsApi* | [**get_transcriptions_for_project**](docs/CustomSpeechProjectsApi.md#get_transcriptions_for_project) | **GET** /projects/{id}/transcriptions | Gets the list of transcriptions for specified project.
*CustomSpeechProjectsApi* | [**update_project**](docs/CustomSpeechProjectsApi.md#update_project) | **PATCH** /projects/{id} | Updates the project identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**create_transcription**](docs/CustomSpeechTranscriptionsApi.md#create_transcription) | **POST** /transcriptions | Creates a new transcription.
*CustomSpeechTranscriptionsApi* | [**delete_transcription**](docs/CustomSpeechTranscriptionsApi.md#delete_transcription) | **DELETE** /transcriptions/{id} | Deletes the specified transcription task.
*CustomSpeechTranscriptionsApi* | [**get_supported_locales_for_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_supported_locales_for_transcriptions) | **GET** /transcriptions/locales | Gets a list of supported locales for offline transcriptions.
*CustomSpeechTranscriptionsApi* | [**get_transcription**](docs/CustomSpeechTranscriptionsApi.md#get_transcription) | **GET** /transcriptions/{id} | Gets the transcription identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**get_transcription_file**](docs/CustomSpeechTranscriptionsApi.md#get_transcription_file) | **GET** /transcriptions/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a transcription (identified with id).
*CustomSpeechTranscriptionsApi* | [**get_transcription_files**](docs/CustomSpeechTranscriptionsApi.md#get_transcription_files) | **GET** /transcriptions/{id}/files | Gets the files of the transcription identified by the given ID.
*CustomSpeechTranscriptionsApi* | [**get_transcriptions**](docs/CustomSpeechTranscriptionsApi.md#get_transcriptions) | **GET** /transcriptions | Gets a list of transcriptions for the authenticated subscription.
*CustomSpeechTranscriptionsApi* | [**update_transcription**](docs/CustomSpeechTranscriptionsApi.md#update_transcription) | **PATCH** /transcriptions/{id} | Updates the mutable details of the transcription identified by its ID.
*CustomSpeechWebHooksApi* | [**create_hook**](docs/CustomSpeechWebHooksApi.md#create_hook) | **POST** /webhooks | Creates a new web hook.
*CustomSpeechWebHooksApi* | [**delete_hook**](docs/CustomSpeechWebHooksApi.md#delete_hook) | **DELETE** /webhooks/{id} | Deletes the web hook identified by the given ID.
*CustomSpeechWebHooksApi* | [**get_hook**](docs/CustomSpeechWebHooksApi.md#get_hook) | **GET** /webhooks/{id} | Gets the web hook identified by the given ID.
*CustomSpeechWebHooksApi* | [**get_hooks**](docs/CustomSpeechWebHooksApi.md#get_hooks) | **GET** /webhooks | Gets the list of web hooks for the authenticated subscription.
*CustomSpeechWebHooksApi* | [**ping_hook**](docs/CustomSpeechWebHooksApi.md#ping_hook) | **POST** /webhooks/{id}/ping | Sends a ping event to the registered URL.
*CustomSpeechWebHooksApi* | [**test_hook**](docs/CustomSpeechWebHooksApi.md#test_hook) | **POST** /webhooks/{id}/test | Sends a request for each registered event type to the registered URL.
*CustomSpeechWebHooksApi* | [**update_hook**](docs/CustomSpeechWebHooksApi.md#update_hook) | **PATCH** /webhooks/{id} | Updates the web hook identified by the given ID.
*ServiceHealthApi* | [**get_health_status**](docs/ServiceHealthApi.md#get_health_status) | **GET** /healthstatus | Returns the overall health of the service and optionally of the different subcomponents.


## Documentation For Models

 - [Component](docs/Component.md)
 - [Dataset](docs/Dataset.md)
 - [DatasetKind](docs/DatasetKind.md)
 - [DatasetLocales](docs/DatasetLocales.md)
 - [DatasetProperties](docs/DatasetProperties.md)
 - [DatasetUpdate](docs/DatasetUpdate.md)
 - [DetailedErrorCode](docs/DetailedErrorCode.md)
 - [Endpoint](docs/Endpoint.md)
 - [EndpointLinks](docs/EndpointLinks.md)
 - [EndpointProperties](docs/EndpointProperties.md)
 - [EndpointPropertiesUpdate](docs/EndpointPropertiesUpdate.md)
 - [EndpointUpdate](docs/EndpointUpdate.md)
 - [EntityError](docs/EntityError.md)
 - [EntityReference](docs/EntityReference.md)
 - [Error](docs/Error.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [Evaluation](docs/Evaluation.md)
 - [EvaluationProperties](docs/EvaluationProperties.md)
 - [EvaluationUpdate](docs/EvaluationUpdate.md)
 - [File](docs/File.md)
 - [FileKind](docs/FileKind.md)
 - [FileLinks](docs/FileLinks.md)
 - [FileProperties](docs/FileProperties.md)
 - [HealthStatus](docs/HealthStatus.md)
 - [InnerError](docs/InnerError.md)
 - [Links](docs/Links.md)
 - [Model](docs/Model.md)
 - [ModelCopy](docs/ModelCopy.md)
 - [ModelDeprecationDates](docs/ModelDeprecationDates.md)
 - [ModelFile](docs/ModelFile.md)
 - [ModelLinks](docs/ModelLinks.md)
 - [ModelManifest](docs/ModelManifest.md)
 - [ModelProperties](docs/ModelProperties.md)
 - [ModelUpdate](docs/ModelUpdate.md)
 - [PaginatedDatasets](docs/PaginatedDatasets.md)
 - [PaginatedEndpoints](docs/PaginatedEndpoints.md)
 - [PaginatedEvaluations](docs/PaginatedEvaluations.md)
 - [PaginatedFiles](docs/PaginatedFiles.md)
 - [PaginatedModels](docs/PaginatedModels.md)
 - [PaginatedProjects](docs/PaginatedProjects.md)
 - [PaginatedTranscriptions](docs/PaginatedTranscriptions.md)
 - [PaginatedWebHooks](docs/PaginatedWebHooks.md)
 - [ProfanityFilterMode](docs/ProfanityFilterMode.md)
 - [Project](docs/Project.md)
 - [ProjectLinks](docs/ProjectLinks.md)
 - [ProjectProperties](docs/ProjectProperties.md)
 - [ProjectUpdate](docs/ProjectUpdate.md)
 - [PunctuationMode](docs/PunctuationMode.md)
 - [ServiceHealth](docs/ServiceHealth.md)
 - [Status](docs/Status.md)
 - [Transcription](docs/Transcription.md)
 - [TranscriptionProperties](docs/TranscriptionProperties.md)
 - [TranscriptionUpdate](docs/TranscriptionUpdate.md)
 - [WebHook](docs/WebHook.md)
 - [WebHookEvents](docs/WebHookEvents.md)
 - [WebHookLinks](docs/WebHookLinks.md)
 - [WebHookProperties](docs/WebHookProperties.md)
 - [WebHookPropertiesUpdate](docs/WebHookPropertiesUpdate.md)
 - [WebHookUpdate](docs/WebHookUpdate.md)


## Documentation For Authorization


## api_key

- **Type**: API key
- **API key parameter name**: Ocp-Apim-Subscription-Key
- **Location**: HTTP header

## token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



