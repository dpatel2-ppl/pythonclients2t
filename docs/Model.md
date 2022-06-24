# Model

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project** | [**EntityReference**](EntityReference.md) |  | [optional] 
**links** | [**ModelLinks**](ModelLinks.md) |  | [optional] 
**properties** | [**ModelProperties**](ModelProperties.md) |  | [optional] 
**_self** | **str** | The location of this entity. | [optional] 
**display_name** | **str** | The display name of the object. | 
**description** | **str** | The description of the object. | [optional] 
**text** | **str** | The text used to adapt this language model. | [optional] 
**base_model** | [**EntityReference**](EntityReference.md) |  | [optional] 
**datasets** | [**list[EntityReference]**](EntityReference.md) | Datasets used for adaptation. | [optional] 
**locale** | **str** | The locale of the contained data. | 
**last_action_date_time** | **datetime** | The time-stamp when the current status was entered.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**created_date_time** | **datetime** | The time-stamp when the object was created.  The time stamp is encoded as ISO 8601 date and time format  (\&quot;YYYY-MM-DDThh:mm:ssZ\&quot;, see https://en.wikipedia.org/wiki/ISO_8601#Combined_date_and_time_representations). | [optional] 
**custom_properties** | **dict(str, str)** | The custom properties of this entity. The maximum allowed key length is 64 characters, the maximum  allowed value length is 256 characters and the count of allowed entries is 10. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


