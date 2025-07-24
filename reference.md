# Reference
<details><summary><code>client.<a href="src/phenoml/client.py">create_fhir_resource_from_text</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language text into a structured FHIR resource
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from phenoml import phenoml

client = phenoml(
    token="YOUR_TOKEN",
)
client.create_fhir_resource_from_text(
    version="R4",
    resource="auto",
    text="Patient has severe asthma with acute exacerbation",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version:** `str` — FHIR version to use
    
</dd>
</dl>

<dl>
<dd>

**resource:** `CreateRequestResource` — Type of FHIR resource to create. Use 'auto' for automatic resource type detection, or specify a supported US Core profile. Recommended to use the supported US Core Profiles for validated results but you can also use any custom profile you've uploaded (if you're a develop or launch customer)
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Natural language text to convert
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/phenoml/client.py">generate_fhir_search_parameters_from_text</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language text into FHIR search parameters
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from phenoml import phenoml

client = phenoml(
    token="YOUR_TOKEN",
)
client.generate_fhir_search_parameters_from_text(
    text="Appointments between March 2-9, 2025",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**text:** `str` — Natural language text to convert into FHIR search parameters
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/phenoml/client.py">upload_custom_fhir_profile</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a custom FHIR StructureDefinition profile for use with the lang2fhir service
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from phenoml import phenoml

client = phenoml(
    token="YOUR_TOKEN",
)
client.upload_custom_fhir_profile(
    version="version",
    resource="custom-patient",
    profile="profile",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version:** `str` — FHIR version that this profile implements
    
</dd>
</dl>

<dl>
<dd>

**resource:** `str` — Name for the custom resource profile (will be converted to lowercase)
    
</dd>
</dl>

<dl>
<dd>

**profile:** `str` — Base64 encoded JSON string of the FHIR StructureDefinition profile
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.<a href="src/phenoml/client.py">convert_document_to_fhir_resource</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts text from a document (PDF or image) and converts it into a structured FHIR resource
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from phenoml import phenoml

client = phenoml(
    token="YOUR_TOKEN",
)
client.convert_document_to_fhir_resource(
    version="R4",
    resource="questionnaire",
    content="content",
    file_type="application/pdf",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version:** `str` — FHIR version to use
    
</dd>
</dl>

<dl>
<dd>

**resource:** `DocumentRequestResource` — Type of FHIR resource to create (questionnaire and US Core questionnaireresponse profiles currently supported)
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — Base64 encoded file content
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `DocumentRequestFileType` — MIME type of the file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

