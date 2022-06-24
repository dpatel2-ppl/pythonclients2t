# swagger_client.CustomSpeechDatasetsForModelAdaptationApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#create_dataset) | **POST** /datasets | Uploads and creates a new dataset by getting the data from a specified URL.
[**delete_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#delete_dataset) | **DELETE** /datasets/{id} | Deletes the specified dataset.
[**get_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset) | **GET** /datasets/{id} | Gets the dataset identified by the given ID.
[**get_dataset_file**](CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset_file) | **GET** /datasets/{id}/files/{fileId} | Gets one specific file (identified with fileId) from a dataset (identified with id).
[**get_dataset_files**](CustomSpeechDatasetsForModelAdaptationApi.md#get_dataset_files) | **GET** /datasets/{id}/files | Gets the files of the dataset identified by the given ID.
[**get_datasets**](CustomSpeechDatasetsForModelAdaptationApi.md#get_datasets) | **GET** /datasets | Gets a list of datasets for the authenticated subscription.
[**get_supported_locales_for_datasets**](CustomSpeechDatasetsForModelAdaptationApi.md#get_supported_locales_for_datasets) | **GET** /datasets/locales | Gets a list of supported locales for datasets.
[**update_dataset**](CustomSpeechDatasetsForModelAdaptationApi.md#update_dataset) | **PATCH** /datasets/{id} | Updates the mutable details of the dataset identified by its ID.
[**upload_dataset_from_form**](CustomSpeechDatasetsForModelAdaptationApi.md#upload_dataset_from_form) | **POST** /datasets/upload | Uploads data and creates a new dataset.


# **create_dataset**
> Dataset create_dataset(dataset)

Uploads and creates a new dataset by getting the data from a specified URL.

### Example
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

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dataset** | [**Dataset**](Dataset.md)| Definition for the new dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_dataset**
> delete_dataset(id)

Deletes the specified dataset.

### Example
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
id = 'id_example' # str | The identifier of the dataset.

try:
    # Deletes the specified dataset.
    api_instance.delete_dataset(id)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->delete_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 

### Return type

void (empty response body)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset**
> Dataset get_dataset(id)

Gets the dataset identified by the given ID.

### Example
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
id = 'id_example' # str | The identifier of the dataset.

try:
    # Gets the dataset identified by the given ID.
    api_response = api_instance.get_dataset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_file**
> File get_dataset_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)

Gets one specific file (identified with fileId) from a dataset (identified with id).

### Example
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
id = 'id_example' # str | The identifier of the dataset.
file_id = 'file_id_example' # str | The identifier of the file.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)

try:
    # Gets one specific file (identified with fileId) from a dataset (identified with id).
    api_response = api_instance.get_dataset_file(id, file_id, sas_validity_in_seconds=sas_validity_in_seconds)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_dataset_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **file_id** | [**str**](.md)| The identifier of the file. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 

### Return type

[**File**](File.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dataset_files**
> PaginatedFiles get_dataset_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)

Gets the files of the dataset identified by the given ID.

### Example
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
id = 'id_example' # str | The identifier of the dataset.
sas_validity_in_seconds = 56 # int | The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. (optional)
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)

try:
    # Gets the files of the dataset identified by the given ID.
    api_response = api_instance.get_dataset_files(id, sas_validity_in_seconds=sas_validity_in_seconds, skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_dataset_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **sas_validity_in_seconds** | **int**| The duration in seconds that an SAS url should be valid. The default duration is 12 hours.              When using BYOS (https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-encryption-of-data-at-rest#bring-your-own-storage-byos-for-customization-and-logging): A value of 0 means that a plain blob URI without SAS token will be generated. | [optional] 
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedFiles**](PaginatedFiles.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_datasets**
> PaginatedDatasets get_datasets(skip=skip, top=top)

Gets a list of datasets for the authenticated subscription.

### Example
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
skip = 56 # int | Number of datasets that will be skipped. (optional)
top = 56 # int | Number of datasets that will be included after skipping. (optional)

try:
    # Gets a list of datasets for the authenticated subscription.
    api_response = api_instance.get_datasets(skip=skip, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_datasets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip** | **int**| Number of datasets that will be skipped. | [optional] 
 **top** | **int**| Number of datasets that will be included after skipping. | [optional] 

### Return type

[**PaginatedDatasets**](PaginatedDatasets.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_supported_locales_for_datasets**
> DatasetLocales get_supported_locales_for_datasets()

Gets a list of supported locales for datasets.

### Example
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

try:
    # Gets a list of supported locales for datasets.
    api_response = api_instance.get_supported_locales_for_datasets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->get_supported_locales_for_datasets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**DatasetLocales**](DatasetLocales.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_dataset**
> Dataset update_dataset(id, dataset_update)

Updates the mutable details of the dataset identified by its ID.

### Example
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
id = 'id_example' # str | The identifier of the dataset.
dataset_update = swagger_client.DatasetUpdate() # DatasetUpdate | The updated values for the dataset.

try:
    # Updates the mutable details of the dataset identified by its ID.
    api_response = api_instance.update_dataset(id, dataset_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->update_dataset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| The identifier of the dataset. | 
 **dataset_update** | [**DatasetUpdate**](DatasetUpdate.md)| The updated values for the dataset. | 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json, application/merge-patch+json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dataset_from_form**
> Dataset upload_dataset_from_form(display_name, locale, kind, project=project, description=description, custom_properties=custom_properties, data=data, email=email)

Uploads data and creates a new dataset.

### Example
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
display_name = 'display_name_example' # str | The name of this dataset (required).
locale = 'locale_example' # str | The locale of this dataset (required).
kind = 'kind_example' # str | The kind of the dataset (required). Possible values are \"Language\", \"Acoustic\", \"Pronunciation\", \"AudioFiles\".
project = 'project_example' # str | The optional string representation of the url of a project. If set, the dataset will be associated with that project. (optional)
description = 'description_example' # str | Optional description of this dataset. (optional)
custom_properties = 'custom_properties_example' # str | The optional custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. (optional)
data = '/path/to/file.txt' # file | For acoustic datasets, a zip file containing the audio data and a text file containing the transcriptions for the audio data. For language datasets, a text file containing the language or pronunciation data. Required in both cases. (optional)
email = 'email_example' # str | An optional string containing the email address to send email notifications to in case the operation completes. The value will be removed after successfully sending the email. (optional)

try:
    # Uploads data and creates a new dataset.
    api_response = api_instance.upload_dataset_from_form(display_name, locale, kind, project=project, description=description, custom_properties=custom_properties, data=data, email=email)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CustomSpeechDatasetsForModelAdaptationApi->upload_dataset_from_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **display_name** | **str**| The name of this dataset (required). | 
 **locale** | **str**| The locale of this dataset (required). | 
 **kind** | **str**| The kind of the dataset (required). Possible values are \&quot;Language\&quot;, \&quot;Acoustic\&quot;, \&quot;Pronunciation\&quot;, \&quot;AudioFiles\&quot;. | 
 **project** | **str**| The optional string representation of the url of a project. If set, the dataset will be associated with that project. | [optional] 
 **description** | **str**| Optional description of this dataset. | [optional] 
 **custom_properties** | **str**| The optional custom properties of this entity. The maximum allowed key length is 64 characters, the maximum allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 
 **data** | **file**| For acoustic datasets, a zip file containing the audio data and a text file containing the transcriptions for the audio data. For language datasets, a text file containing the language or pronunciation data. Required in both cases. | [optional] 
 **email** | **str**| An optional string containing the email address to send email notifications to in case the operation completes. The value will be removed after successfully sending the email. | [optional] 

### Return type

[**Dataset**](Dataset.md)

### Authorization

[api_key](../README.md#api_key), [token](../README.md#token)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

