# Reference
## Agent
<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new PhenoAgent with specified configuration
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
client.agent.create(
    name="name",
    prompts=["prompt_123", "prompt_456"],
    is_active=True,
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

**name:** `str` — Agent name
    
</dd>
</dl>

<dl>
<dd>

**prompts:** `typing.Sequence[str]` — Array of prompt IDs to use for this agent
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `bool` — Whether the agent is active
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Agent description
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[str]]` — Array of MCP server tool IDs to use for this agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the agent
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[AgentCreateRequestProvider]` — FHIR provider ID(s) - must be valid UUIDs from existing FHIR providers
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of PhenoAgents belonging to the authenticated user
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
client.agent.list()

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

**is_active:** `typing.Optional[bool]` — Filter by active status
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[str]` — Filter by tags
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific agent by its ID
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
client.agent.get(
    id="id",
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

**id:** `str` — Agent ID
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing agent's configuration
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
client.agent.update(
    id="id",
    name="name",
    prompts=["prompt_123", "prompt_456"],
    is_active=True,
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

**id:** `str` — Agent ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Agent name
    
</dd>
</dl>

<dl>
<dd>

**prompts:** `typing.Sequence[str]` — Array of prompt IDs to use for this agent
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `bool` — Whether the agent is active
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Agent description
    
</dd>
</dl>

<dl>
<dd>

**tools:** `typing.Optional[typing.Sequence[str]]` — Array of MCP server tool IDs to use for this agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the agent
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[AgentCreateRequestProvider]` — FHIR provider ID(s) - must be valid UUIDs from existing FHIR providers
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes an existing agent
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
client.agent.delete(
    id="id",
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

**id:** `str` — Agent ID
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing agent's configuration
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
from phenoml.agent import JsonPatchOperation

client = phenoml(
    token="YOUR_TOKEN",
)
client.agent.patch(
    id="id",
    request=[
        JsonPatchOperation(
            op="replace",
            path="/name",
            value="Updated Agent Name",
        ),
        JsonPatchOperation(
            op="add",
            path="/tags/-",
            value="new-tag",
        ),
        JsonPatchOperation(
            op="remove",
            path="/description",
        ),
    ],
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

**id:** `str` — Agent ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `JsonPatch` 
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">chat</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to an agent and receive a response
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
client.agent.chat(
    message="What is the patient's current condition?",
    agent_id="agent-123",
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

**message:** `str` — The message to send to the agent
    
</dd>
</dl>

<dl>
<dd>

**agent_id:** `str` — The ID of the agent to chat with
    
</dd>
</dl>

<dl>
<dd>

**context:** `typing.Optional[str]` — Optional context for the conversation
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `typing.Optional[str]` — Optional session ID for conversation continuity
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">get_chat_messages</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of chat messages for a given chat session
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
client.agent.get_chat_messages(
    chat_session_id="chat_session_id",
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

**chat_session_id:** `str` — Chat session ID
    
</dd>
</dl>

<dl>
<dd>

**num_messages:** `typing.Optional[int]` — Number of messages to return
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Filter by role
    
</dd>
</dl>

<dl>
<dd>

**order:** `typing.Optional[AgentGetChatMessagesRequestOrder]` — Order of messages
    
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

## Agent Prompts
<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new agent prompt
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
client.agent.prompts.create(
    name="Medical Assistant System Prompt",
    content="You are a helpful medical assistant specialized in FHIR data processing...",
    is_active=True,
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

**name:** `str` — Prompt name
    
</dd>
</dl>

<dl>
<dd>

**content:** `str` — Prompt content
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `bool` — Whether the prompt is active
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Prompt description
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` — Whether this is a default prompt
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the prompt
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of agent prompts belonging to the authenticated user
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
client.agent.prompts.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific prompt by its ID
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
client.agent.prompts.get(
    id="id",
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

**id:** `str` — Prompt ID
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing prompt
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
client.agent.prompts.update(
    id="id",
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

**id:** `str` — Prompt ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Prompt name
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Prompt description
    
</dd>
</dl>

<dl>
<dd>

**content:** `typing.Optional[str]` — Prompt content
    
</dd>
</dl>

<dl>
<dd>

**is_default:** `typing.Optional[bool]` — Whether this is a default prompt
    
</dd>
</dl>

<dl>
<dd>

**is_active:** `typing.Optional[bool]` — Whether the prompt is active
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the prompt
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a prompt by setting is_active to false
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
client.agent.prompts.delete(
    id="id",
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

**id:** `str` — Prompt ID
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Patches an existing prompt
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
from phenoml.agent import JsonPatchOperation

client = phenoml(
    token="YOUR_TOKEN",
)
client.agent.prompts.patch(
    id="id",
    request=[
        JsonPatchOperation(
            op="replace",
            path="/name",
            value="Updated Agent Name",
        ),
        JsonPatchOperation(
            op="add",
            path="/tags/-",
            value="new-tag",
        ),
        JsonPatchOperation(
            op="remove",
            path="/description",
        ),
    ],
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

**id:** `str` — Agent Prompt ID
    
</dd>
</dl>

<dl>
<dd>

**request:** `JsonPatch` 
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">load_defaults</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads default agent prompts for the authenticated user
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
client.agent.prompts.load_defaults()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Authtoken Auth
<details><summary><code>client.authtoken.auth.<a href="src/phenoml/authtoken/auth/client.py">generate_token</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Obtain an access token using client credentials
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
client.authtoken.auth.generate_token(
    username="username",
    password="password",
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

**username:** `str` — The user's username or email
    
</dd>
</dl>

<dl>
<dd>

**password:** `str` — The user's password
    
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

## Cohort
<details><summary><code>client.cohort.<a href="src/phenoml/cohort/client.py">analyze</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language text into structured FHIR search queries for patient cohort analysis
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
client.cohort.analyze(
    text="female patients over 65 with diabetes but not hypertension",
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

**text:** `str` — Natural language text describing patient cohort criteria
    
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

## Construe
<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">upload_code_system</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Upload a custom medical code system with codes and descriptions for use in code extraction.
Upon upload, construe generates embeddings for all of the codes in the code system and stores them in the vector database so you can
subsequently use the code system for construe/extract and lang2fhir/create (coming soon!)
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
client.construe.upload_code_system(
    name="CUSTOM_CODES",
    version="1.0",
    format="json",
    file="file",
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

**name:** `str` — Name of the code system
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the code system
    
</dd>
</dl>

<dl>
<dd>

**format:** `UploadRequestFormat` — Format of the uploaded file
    
</dd>
</dl>

<dl>
<dd>

**file:** `str` — The file contents as a base64-encoded string
    
</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[float]` — Optional revision number
    
</dd>
</dl>

<dl>
<dd>

**code_col:** `typing.Optional[str]` — Column name containing codes (required for CSV format)
    
</dd>
</dl>

<dl>
<dd>

**desc_col:** `typing.Optional[str]` — Column name containing descriptions (required for CSV format)
    
</dd>
</dl>

<dl>
<dd>

**defn_col:** `typing.Optional[str]` — Optional column name containing long definitions (for CSV format)
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">extract_codes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language text into structured medical codes
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
client.construe.extract_codes(
    text="Patient is a 14-year-old female, previously healthy, who is here for evaluation of abnormal renal ultrasound with atrophic right kidney",
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

**text:** `str` — Natural language text to extract codes from
    
</dd>
</dl>

<dl>
<dd>

**system:** `typing.Optional[ExtractRequestSystem]` 
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[ExtractRequestConfig]` 
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">cohort</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a patient cohort based on a natural language description.
Translates the description into FHIR search queries and optional SQL queries.
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
client.construe.cohort(
    text="Between 20 and 40 years old with hyperlipidemia",
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

**text:** `str` — Natural language description of the desired patient cohort.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[ConstrueCohortRequestConfig]` 
    
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

## Fhir
<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves FHIR resources from the specified provider. Supports both individual resource retrieval and search operations based on the FHIR path and query parameters.

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
client.fhir.search(
    fhir_provider_id="fhir_provider_id",
    fhir_path="fhir_path",
    phenoml_on_behalf_of="user@example.com",
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**fhir_path:** `str` 

The FHIR resource path to operate on. This follows FHIR RESTful API conventions.
Examples:
- "Patient" (for resource type operations)
- "Patient/123" (for specific resource operations)
- "Patient/123/_history" (for history operations)
    
</dd>
</dl>

<dl>
<dd>

**query_parameters:** `typing.Optional[typing.Dict[str, typing.Optional[str]]]` 

FHIR-compliant query parameters for search operations. Supports standard FHIR search parameters including:
- Resource-specific search parameters (e.g., name for Patient, status for Observation)
- Common search parameters (_id, _lastUpdated, _tag, _profile, _security, _text, _content, _filter)
- Result parameters (_count, _offset, _sort, _include, _revinclude, _summary, _elements)
- Search prefixes for dates, numbers, quantities (eq, ne, gt, ge, lt, le, sa, eb, ap)
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new FHIR resource on the specified provider. The request body should contain a valid FHIR resource in JSON format.

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
client.fhir.create(
    fhir_provider_id="fhir_provider_id",
    fhir_path="fhir_path",
    phenoml_on_behalf_of="user@example.com",
    resource_type="Patient",
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**fhir_path:** `str` 

The FHIR resource path to operate on. This follows FHIR RESTful API conventions.
Examples:
- "Patient" (for resource type operations)
- "Patient/123" (for specific resource operations)
- "Patient/123/_history" (for history operations)
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — The type of FHIR resource (e.g., Patient, Observation, etc.)
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Logical ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[FhirResourceMeta]` — Metadata about the resource
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">upsert</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates or updates a FHIR resource on the specified provider. If the resource exists, it will be updated; otherwise, it will be created.

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
client.fhir.upsert(
    fhir_provider_id="fhir_provider_id",
    fhir_path="fhir_path",
    phenoml_on_behalf_of="user@example.com",
    resource_type="Patient",
    id="123",
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**fhir_path:** `str` 

The FHIR resource path to operate on. This follows FHIR RESTful API conventions.
Examples:
- "Patient" (for resource type operations)
- "Patient/123" (for specific resource operations)
- "Patient/123/_history" (for history operations)
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `str` — The type of FHIR resource (e.g., Patient, Observation, etc.)
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — Logical ID of the resource
    
</dd>
</dl>

<dl>
<dd>

**meta:** `typing.Optional[FhirResourceMeta]` — Metadata about the resource
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a FHIR resource from the specified provider.

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
client.fhir.delete(
    fhir_provider_id="fhir_provider_id",
    fhir_path="fhir_path",
    phenoml_on_behalf_of="user@example.com",
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**fhir_path:** `str` 

The FHIR resource path to operate on. This follows FHIR RESTful API conventions.
Examples:
- "Patient" (for resource type operations)
- "Patient/123" (for specific resource operations)
- "Patient/123/_history" (for history operations)
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">patch</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially updates a FHIR resource on the specified provider using JSON Patch operations as defined in RFC 6902.

The request body should contain an array of JSON Patch operations. Each operation specifies:
- `op`: The operation type (add, remove, replace, move, copy, test)
- `path`: JSON Pointer to the target location in the resource
- `value`: The value to use (required for add, replace, and test operations)

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
from phenoml.fhir import FhirPatchRequestBodyItem

client = phenoml(
    token="YOUR_TOKEN",
)
client.fhir.patch(
    fhir_provider_id="fhir_provider_id",
    fhir_path="fhir_path",
    phenoml_on_behalf_of="user@example.com",
    request=[
        FhirPatchRequestBodyItem(
            op="test",
            path="/gender",
            value="male",
        ),
        FhirPatchRequestBodyItem(
            op="replace",
            path="/gender",
            value="female",
        ),
    ],
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**fhir_path:** `str` 

The FHIR resource path to operate on. This follows FHIR RESTful API conventions.
Examples:
- "Patient" (for resource type operations)
- "Patient/123" (for specific resource operations)
- "Patient/123/_history" (for history operations)
    
</dd>
</dl>

<dl>
<dd>

**request:** `typing.Sequence[FhirPatchRequestBodyItem]` 
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">execute_bundle</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes a FHIR Bundle transaction or batch operation on the specified provider. This allows multiple FHIR resources to be processed in a single request.

The request body should contain a valid FHIR Bundle resource with transaction or batch type.

The request is proxied to the configured FHIR server with appropriate authentication headers.
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
from phenoml.fhir import FhirBundleEntryItem, FhirBundleEntryItemRequest

client = phenoml(
    token="YOUR_TOKEN",
)
client.fhir.execute_bundle(
    fhir_provider_id="fhir_provider_id",
    phenoml_on_behalf_of="user@example.com",
    entry=[
        FhirBundleEntryItem(
            resource={
                "resourceType": "Patient",
                "name": [{"family": "Doe", "given": ["John"]}],
            },
            request=FhirBundleEntryItemRequest(
                method="POST",
                url="Patient",
            ),
        ),
        FhirBundleEntryItem(
            resource={
                "resourceType": "Observation",
                "status": "final",
                "subject": {"reference": "Patient/123"},
            },
            request=FhirBundleEntryItemRequest(
                method="POST",
                url="Observation",
            ),
        ),
    ],
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

**fhir_provider_id:** `str` 

The ID of the FHIR provider to use. Can be either:
- A UUID representing the provider ID
- A provider name (legacy support - will just use the most recently updated provider with this name)
    
</dd>
</dl>

<dl>
<dd>

**entry:** `typing.Sequence[FhirBundleEntryItem]` — Array of bundle entries containing resources or operation results
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` — Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
    
</dd>
</dl>

<dl>
<dd>

**total:** `typing.Optional[int]` 

Total number of resources that match the search criteria.
Optional field as not all FHIR servers include it (e.g., Medplum).
    
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

## FhirProvider
<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new FHIR provider configuration with authentication credentials
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
client.fhir_provider.create(
    name="Epic Sandbox",
    provider="athenahealth",
    auth_method="client_secret",
    base_url="https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4",
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

**name:** `str` — Display name for the FHIR provider
    
</dd>
</dl>

<dl>
<dd>

**provider:** `Provider` 
    
</dd>
</dl>

<dl>
<dd>

**auth_method:** `AuthMethod` 
    
</dd>
</dl>

<dl>
<dd>

**base_url:** `str` — Base URL of the FHIR server
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the FHIR provider
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — OAuth client ID (required for most auth methods)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OAuth client secret (required for client_secret and on_behalf_of auth methods)
    
</dd>
</dl>

<dl>
<dd>

**service_account_key:** `typing.Optional[ServiceAccountKey]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[str]` — OAuth scopes to request
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a list of all active FHIR providers for the authenticated user
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
client.fhir_provider.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific FHIR provider configuration by its ID
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
client.fhir_provider.get(
    fhir_provider_id="fhir_provider_id",
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

**fhir_provider_id:** `str` — ID of the FHIR provider to retrieve
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Soft deletes a FHIR provider by setting is_active to false
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
client.fhir_provider.delete(
    fhir_provider_id="fhir_provider_id",
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

**fhir_provider_id:** `str` — ID of the FHIR provider to delete
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">add_auth_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Adds a new authentication configuration to an existing FHIR provider. This enables key rotation and multiple auth configurations per provider.
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
client.fhir_provider.add_auth_config(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    auth_method="client_secret",
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

**fhir_provider_id:** `str` — ID of the FHIR provider to add auth config to
    
</dd>
</dl>

<dl>
<dd>

**auth_method:** `AuthMethod` 
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — OAuth client secret (required for client_secret and on_behalf_of auth methods)
    
</dd>
</dl>

<dl>
<dd>

**service_account_key:** `typing.Optional[ServiceAccountKey]` 
    
</dd>
</dl>

<dl>
<dd>

**credential_expiry:** `typing.Optional[dt.datetime]` — Expiry time for JWT credentials (only applicable for JWT auth method)
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[str]` — OAuth scopes to request
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">set_active_auth_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Sets which authentication configuration should be active for a FHIR provider. Only one auth config can be active at a time.
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
client.fhir_provider.set_active_auth_config(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    auth_config_id="auth-config-123",
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

**fhir_provider_id:** `str` — ID of the FHIR provider
    
</dd>
</dl>

<dl>
<dd>

**auth_config_id:** `str` — ID of the auth configuration to set as active
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">remove_auth_config</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes an authentication configuration from a FHIR provider. Cannot remove the currently active auth configuration.
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
client.fhir_provider.remove_auth_config(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    auth_config_id="auth-config-123",
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

**fhir_provider_id:** `str` — ID of the FHIR provider
    
</dd>
</dl>

<dl>
<dd>

**auth_config_id:** `str` — ID of the auth configuration to remove
    
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

## Lang2Fhir
<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">create</a>(...)</code></summary>
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
client.lang2fhir.create(
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">search</a>(...)</code></summary>
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
client.lang2fhir.search(
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">upload_profile</a>(...)</code></summary>
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
client.lang2fhir.upload_profile(
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">document</a>(...)</code></summary>
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
client.lang2fhir.document(
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

## Tools
<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">create_fhir_resource</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language to FHIR resource and optionally stores it in a FHIR server
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
client.tools.create_fhir_resource(
    resource="auto",
    text="Patient John Doe has severe asthma with acute exacerbation",
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

**resource:** `Lang2FhirAndCreateRequestResource` — Type of FHIR resource to create. Use 'auto' for automatic resource type detection, or specify a supported US Core profile.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Natural language text to convert to FHIR resource
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — FHIR provider ID - must be a valid UUID from existing FHIR providers. also supports provider by name (e.g. medplum)
    
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">search_fhir_resources</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language to FHIR search parameters and executes search in FHIR server
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
client.tools.search_fhir_resources(
    text="Find all appointments for patient John Doe next week",
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

**text:** `str` — Natural language text to convert to FHIR search parameters
    
</dd>
</dl>

<dl>
<dd>

**patient_id:** `typing.Optional[str]` — Patient ID to filter results
    
</dd>
</dl>

<dl>
<dd>

**practitioner_id:** `typing.Optional[str]` — Practitioner ID to filter results
    
</dd>
</dl>

<dl>
<dd>

**count:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — FHIR provider ID - must be a valid UUID from existing FHIR providers. also supports provider by name (e.g. medplum)
    
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">analyze_cohort</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Uses LLM to extract search concepts from natural language and builds patient cohorts with inclusion/exclusion criteria
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
client.tools.analyze_cohort(
    text="female patients over 20 with diabetes but not hypertension",
    provider="550e8400-e29b-41d4-a716-446655440000",
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

**text:** `str` — Natural language text describing the patient cohort criteria
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — FHIR provider ID - must be a valid UUID from existing FHIR providers. also supports provider by name (e.g. medplum)
    
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

## Tools McpServer
<details><summary><code>client.tools.mcp_server.<a href="src/phenoml/tools/mcp_server/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new MCP server
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
client.tools.mcp_server.create(
    name="My MCP Server",
    mcp_server_url="https://mcp.example.com",
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

**name:** `str` — Name of the MCP server
    
</dd>
</dl>

<dl>
<dd>

**mcp_server_url:** `str` — URL of the MCP server
    
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

<details><summary><code>client.tools.mcp_server.<a href="src/phenoml/tools/mcp_server/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all MCP servers for a specific user
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
client.tools.mcp_server.list()

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

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tools.mcp_server.<a href="src/phenoml/tools/mcp_server/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a MCP server by ID
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
client.tools.mcp_server.get(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` — ID of the MCP server to retrieve
    
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

<details><summary><code>client.tools.mcp_server.<a href="src/phenoml/tools/mcp_server/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a MCP server by ID
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
client.tools.mcp_server.delete(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` — ID of the MCP server to delete
    
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

## Tools McpServer Tools
<details><summary><code>client.tools.mcp_server.tools.<a href="src/phenoml/tools/mcp_server/tools/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all MCP server tools for a specific MCP server
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
client.tools.mcp_server.tools.list(
    mcp_server_id="mcp_server_id",
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

**mcp_server_id:** `str` — ID of the MCP server to list tools for
    
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

<details><summary><code>client.tools.mcp_server.tools.<a href="src/phenoml/tools/mcp_server/tools/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a MCP server tool by ID
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
client.tools.mcp_server.tools.get(
    mcp_server_tool_id="mcp_server_tool_id",
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

**mcp_server_tool_id:** `str` — ID of the MCP server tool to retrieve
    
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

<details><summary><code>client.tools.mcp_server.tools.<a href="src/phenoml/tools/mcp_server/tools/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a MCP server tool by ID
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
client.tools.mcp_server.tools.delete(
    mcp_server_tool_id="mcp_server_tool_id",
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

**mcp_server_tool_id:** `str` — ID of the MCP server tool to delete
    
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

<details><summary><code>client.tools.mcp_server.tools.<a href="src/phenoml/tools/mcp_server/tools/client.py">call</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Calls a MCP server tool
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
client.tools.mcp_server.tools.call(
    mcp_server_tool_id="mcp_server_tool_id",
    arguments={"title": "PhenoML Agent API"},
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

**mcp_server_tool_id:** `str` — ID of the MCP server tool to call
    
</dd>
</dl>

<dl>
<dd>

**arguments:** `typing.Dict[str, typing.Optional[typing.Any]]` — Arguments to pass to the MCP server tool
    
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

