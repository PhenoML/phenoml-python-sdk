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
    provider="provider",
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

**provider:** `AgentCreateRequestProvider` 

FHIR provider ID(s) for this agent. Required.
In shared/experiment environments, the default sandbox provider is used if a different provider is not explicitly specified.
    
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

**workflows:** `typing.Optional[typing.Sequence[str]]` — Array of workflow IDs to expose as tools for this agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the agent
    
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
client.agent.list(
    tags="tags",
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
    provider="provider",
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

**provider:** `AgentCreateRequestProvider` 

FHIR provider ID(s) for this agent. Required.
In shared/experiment environments, the default sandbox provider is used if a different provider is not explicitly specified.
    
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

**workflows:** `typing.Optional[typing.Sequence[str]]` — Array of workflow IDs to expose as tools for this agent
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Sequence[str]]` — Tags for categorizing the agent
    
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
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    num_messages=1,
    role="user",
    order="asc",
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

**role:** `typing.Optional[AgentGetChatMessagesRequestRole]` 

Filter by one or more message roles. Multiple roles can be specified as a comma-separated string.
If not specified, messages with all roles are returned.

**Available roles:**
- `user` - Messages from the user
- `assistant` - Text responses from the AI assistant
- `model` - Function/tool call requests from the model
- `function` - Function/tool call results
    
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

Deletes a prompt
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

Upload a custom medical code system with codes and descriptions for use in code extraction. Requires a paid plan.
Returns 202 immediately; embedding generation runs asynchronously. Poll
GET /construe/codes/systems/{codesystem}?version={version} to check when status
transitions from "processing" to "ready" or "failed".
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
    format="csv",
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

**name:** `str` 

Name of the code system. Names are case-insensitive and stored uppercase.
Builtin system names (e.g. ICD-10-CM, SNOMED_CT_US_LITE, LOINC, CPT, etc.) are
reserved and cannot be used for custom uploads; attempts return HTTP 403 Forbidden.
    
</dd>
</dl>

<dl>
<dd>

**version:** `str` — Version of the code system
    
</dd>
</dl>

<dl>
<dd>

**format:** `UploadRequestFormat` — Upload format
    
</dd>
</dl>

<dl>
<dd>

**revision:** `typing.Optional[float]` — Optional revision number
    
</dd>
</dl>

<dl>
<dd>

**file:** `typing.Optional[str]` 

The file contents as a base64-encoded string.
For CSV format, this is the CSV file contents.
For JSON format, this is a base64-encoded JSON array; prefer using 'codes' instead.
    
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

**codes:** `typing.Optional[typing.Sequence[CodeResponse]]` 

The codes to upload as a JSON array (JSON format only).
This is the preferred way to upload JSON codes, as it avoids unnecessary base64 encoding.
If both 'codes' and 'file' are provided, 'codes' takes precedence.
    
</dd>
</dl>

<dl>
<dd>

**replace:** `typing.Optional[bool]` 

If true, replaces an existing code system with the same name and version.
Builtin systems cannot be replaced; attempts to do so return HTTP 403 Forbidden.
When false (default), uploading a duplicate returns 409 Conflict.
    
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

Converts natural language text into structured medical codes.

Usage of CPT is subject to AMA requirements: see PhenoML Terms of Service.
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">list_available_code_systems</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the terminology server's catalog of available code systems, including both built-in standard terminologies and custom uploaded systems.
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
client.construe.list_available_code_systems()

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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">get_code_system_detail</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns full metadata for a single code system, including timestamps and builtin status.
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
client.construe.get_code_system_detail(
    codesystem="ICD-10-CM",
    version="2025",
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

**codesystem:** `str` — Code system name (e.g., "ICD-10-CM", "SNOMED_CT_US_LITE")
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system. Required if multiple versions exist.
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">delete_custom_code_system</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a custom (non-builtin) code system and all its codes. Builtin systems cannot be deleted.
Only available on dedicated instances. Large systems may take up to a minute to delete.
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
client.construe.delete_custom_code_system(
    codesystem="CUSTOM_CODES",
    version="version",
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

**codesystem:** `str` — Code system name
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system. Required if multiple versions exist.
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">export_custom_code_system</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exports a custom (non-builtin) code system as a JSON file compatible with the upload format.
The exported file can be re-uploaded directly via POST /construe/upload with format "json".
Only available on dedicated instances. Builtin systems cannot be exported.
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
client.construe.export_custom_code_system(
    codesystem="CUSTOM_CODES",
    version="version",
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

**codesystem:** `str` — Code system name
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system. Required if multiple versions exist.
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">list_codes_in_a_code_system</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of all codes in the specified code system from the terminology server.

Usage of CPT is subject to AMA requirements: see PhenoML Terms of Service.
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
client.construe.list_codes_in_a_code_system(
    codesystem="ICD-10-CM",
    version="2025",
    cursor="cursor",
    limit=1,
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

**codesystem:** `str` — Code system name (e.g., "ICD-10-CM", "SNOMED_CT_US_LITE")
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system. Required if multiple versions exist.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from previous response
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of codes to return (default 20)
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">get_a_specific_code</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Looks up a specific code in the terminology server and returns its details.

Usage of CPT is subject to AMA requirements: see PhenoML Terms of Service.
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
client.construe.get_a_specific_code(
    codesystem="ICD-10-CM",
    code_id="E11.65",
    version="version",
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

**codesystem:** `str` — Code system name
    
</dd>
</dl>

<dl>
<dd>

**code_id:** `str` — The code identifier
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">semantic_search_embedding_based</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs semantic similarity search using vector embeddings.

**Availability**: This endpoint works for both **built-in and custom** code systems.

**When to use**: Best for natural language queries where you want to find conceptually
related codes, even when different terminology is used. The search understands meaning,
not just keywords.

**Examples**:
- Query "trouble breathing at night" finds codes like "Sleep apnea", "Orthopnea",
  "Nocturnal dyspnea" — semantically related but no exact keyword matches
- Query "heart problems" finds "Myocardial infarction", "Cardiac arrest", "Arrhythmia"

**Trade-offs**: Slower than text search (requires embedding generation), but finds
conceptually similar results that keyword search would miss.

See also: `/search/text` for faster keyword-based lookup with typo tolerance.

Usage of CPT is subject to AMA requirements: see PhenoML Terms of Service.
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
client.construe.semantic_search_embedding_based(
    codesystem="ICD-10-CM",
    text="patient has trouble breathing at night and wakes up gasping",
    version="version",
    limit=1,
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

**codesystem:** `str` — Code system name
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — Natural language text to find semantically similar codes for
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (default 10, max 50)
    
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

<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">terminology_server_text_search</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs fast full-text search over code IDs and descriptions.

**Availability**: This endpoint is only available for **built-in code systems**.
Custom code systems uploaded via `/construe/upload` are not indexed for full-text search
and will return empty results. Use `/search/semantic` to search custom code systems.

**When to use**: Best for autocomplete UIs, code lookup, or when users know part of
the code ID or specific keywords. Fast response times suitable for typeahead interfaces.

**Features**:
- Substring matching on code IDs (e.g., "11.65" finds "E11.65")
- Typo tolerance on descriptions (not on code IDs)
- Fast response times (~10-50ms)

**Examples**:
- Query "E11" finds all codes starting with E11 (diabetes codes)
- Query "diabtes" (typo) still finds "diabetes" codes

**Trade-offs**: Faster than semantic search, but only matches keywords/substrings.
Won't find conceptually related codes with different terminology.

See also: `/search/semantic` for finding conceptually similar codes.

Usage of CPT is subject to AMA requirements: see PhenoML Terms of Service.
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
client.construe.terminology_server_text_search(
    codesystem="ICD-10-CM",
    q="E11.65",
    version="version",
    limit=1,
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

**codesystem:** `str` — Code system name
    
</dd>
</dl>

<dl>
<dd>

**q:** `str` — Search query (searches code IDs and descriptions)
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — Specific version of the code system
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results (default 20, max 100)
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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

Creates a new FHIR provider configuration with authentication credentials.

Note: The "sandbox" provider type cannot be created via this API - it is managed internally.
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

**role:** `typing.Optional[Role]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[str]` — OAuth scopes to request. Cannot be specified with role. If neither role nor scopes are specified, the provider-specific default role will be used. You are solely responsible for ensuring the scopes are valid options for the provider being created or updated.
    
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

Retrieves a list of all active FHIR providers for the authenticated user.

On shared instances, only sandbox providers are returned.
Sandbox providers return FhirProviderSandboxInfo.
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

Retrieves a specific FHIR provider configuration by its ID.

Sandbox providers return FhirProviderSandboxInfo.
On shared instances, only sandbox providers can be accessed.
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

Soft deletes a FHIR provider by setting is_active to false.

Note: Sandbox providers cannot be deleted.
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

Adds a new authentication configuration to an existing FHIR provider.
This enables key rotation and multiple auth configurations per provider.

Note: Sandbox providers cannot be modified.
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

**role:** `typing.Optional[Role]` 
    
</dd>
</dl>

<dl>
<dd>

**scopes:** `typing.Optional[str]` — OAuth scopes to request. Cannot be specified with role. If neither role nor scopes are specified, the provider-specific default role will be used. You are solely responsible for ensuring the scopes are valid options for the provider being created or updated.
    
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

Sets which authentication configuration should be active for a FHIR provider.
Only one auth config can be active at a time.

If the specified auth config is already active, the request succeeds without
making any changes and returns a message indicating the config is already active.

Note: Sandbox providers cannot be modified.
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

Removes an authentication configuration from a FHIR provider.
Cannot remove the currently active auth configuration.

Note: Sandbox providers cannot be modified.
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">create_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyzes natural language text and extracts multiple FHIR resources, returning them as a transaction Bundle.
Automatically detects Patient, Condition, MedicationRequest, Observation, and other resource types from the text.
Resources are linked with proper references (e.g., Conditions reference the Patient).
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
client.lang2fhir.create_multi(
    text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
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

**text:** `str` — Natural language text containing multiple clinical concepts to extract
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — FHIR version to use
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Optional FHIR provider name for provider-specific profiles
    
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

Converts natural language text into FHIR search parameters.
Automatically identifies the appropriate FHIR resource type and generates valid search query parameters.

Supported resource types include: AllergyIntolerance, Appointment, CarePlan, CareTeam, Condition,
Coverage, Device, DiagnosticReport, DocumentReference, Encounter, Goal, Immunization, Location,
Medication, MedicationRequest, Observation, Organization, Patient, PlanDefinition, Practitioner,
PractitionerRole, Procedure, Provenance, Questionnaire, QuestionnaireResponse, RelatedPerson,
Schedule, ServiceRequest, Slot, and Specimen.
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

**text:** `str` 

Natural language text to convert into FHIR search parameters.
The system will automatically identify the appropriate resource type and generate valid search parameters.

Examples:
- "Appointments between March 2-9, 2025" → Appointment search with date range
- "Patients with diabetes" → Condition search with code parameter
- "Active medication requests for metformin" → MedicationRequest search
- "Lab results for creatinine" → DiagnosticReport search
- "Dr. Smith's schedule" → Practitioner or Schedule search
    
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

Upload a custom FHIR StructureDefinition profile for use with the lang2fhir service.

All metadata is derived from the StructureDefinition JSON itself. The lowercase `id` field
from the StructureDefinition is used as the profile's unique identifier and lookup key.
To use the uploaded profile with `/lang2fhir/create`, pass this id as the `resource` parameter.

Uploads will be rejected if:
- A built-in US Core or R4 base profile already exists with the same id
- A custom profile with the same id has already been uploaded
- A custom profile with the same url has already been uploaded
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
    profile="(base64 encoded FHIR StructureDefinition JSON)",
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

**profile:** `str` — Base64 encoded JSON string of a FHIR StructureDefinition. The profile must include id, url, type, and a snapshot with elements. All metadata (version, resource type, identifier) is derived from the StructureDefinition itself. The lowercase id from the StructureDefinition becomes the profile's lookup key.
    
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

**content:** `str` 

Base64 encoded file content.
Supported file types: PDF (application/pdf), PNG (image/png), JPEG (image/jpeg).
File type is auto-detected from content magic bytes.
    
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

## Summary
<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">list_templates</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all summary templates for the authenticated user
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
client.summary.list_templates()

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

<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">create_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a summary template from an example using LLM function calling
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
client.summary.create_template(
    name="name",
    example_summary="Patient John Doe, age 45, presents with hypertension diagnosed on 2024-01-15.",
    target_resources=["Patient", "Condition", "Observation"],
    mode="mode",
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

**name:** `str` — Name of the template
    
</dd>
</dl>

<dl>
<dd>

**example_summary:** `str` — Example summary note to generate template from
    
</dd>
</dl>

<dl>
<dd>

**target_resources:** `typing.Sequence[str]` — List of target FHIR resources
    
</dd>
</dl>

<dl>
<dd>

**mode:** `str` — Template mode (stored with the template)
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Description of the template
    
</dd>
</dl>

<dl>
<dd>

**example_fhir_data:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional example FHIR data that corresponds to the example summary
    
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

<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">get_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a specific summary template
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
client.summary.get_template(
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

**id:** `str` — Template ID
    
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

<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">update_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing summary template
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
client.summary.update_template(
    id="id",
    name="name",
    template="template",
    target_resources=["target_resources"],
    mode="mode",
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

**id:** `str` — Template ID
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**template:** `str` — Updated template with placeholders
    
</dd>
</dl>

<dl>
<dd>

**target_resources:** `typing.Sequence[str]` 
    
</dd>
</dl>

<dl>
<dd>

**mode:** `str` — Template mode
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` 
    
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

<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">delete_template</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a summary template
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
client.summary.delete_template(
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

**id:** `str` — Template ID
    
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

<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a summary from FHIR resources using one of three modes:
- **narrative**: Uses a template to substitute FHIR data into placeholders (requires template_id)
- **flatten**: Flattens FHIR resources into a searchable format for RAG/search (no template needed)
- **ips**: Generates an International Patient Summary (IPS) narrative per ISO 27269/HL7 FHIR IPS IG. Requires a Bundle with exactly one Patient resource (returns 400 error if no Patient or multiple Patients are present). Automatically filters resources to those referencing the patient and generates sections for allergies, medications, problems, immunizations, procedures, and vital signs.
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
from phenoml.summary import FhirResource

client = phenoml(
    token="YOUR_TOKEN",
)
client.summary.create(
    fhir_resources=FhirResource(
        resource_type="resourceType",
    ),
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

**fhir_resources:** `CreateSummaryRequestFhirResources` 

FHIR resources (single resource or Bundle).
For IPS mode, must be a Bundle containing exactly one Patient resource with at least one
identifier (id, fullUrl, or identifier field). Returns an error if no Patient is found,
if multiple Patients are present, or if the Patient has no identifiers. Resources are
automatically filtered to only include those referencing the patient.
    
</dd>
</dl>

<dl>
<dd>

**mode:** `typing.Optional[CreateSummaryRequestMode]` 

Summary generation mode:
- narrative: Substitute FHIR data into a template (requires template_id)
- flatten: Flatten FHIR resources for RAG/search (no template needed)
- ips: Generate International Patient Summary (IPS) narrative per ISO 27269/HL7 FHIR IPS IG
    
</dd>
</dl>

<dl>
<dd>

**template_id:** `typing.Optional[str]` — ID of the template to use (required for narrative mode)
    
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
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">create_fhir_resources_multi</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts multiple FHIR resources from natural language text and stores them in a FHIR server.
Automatically detects Patient, Condition, MedicationRequest, Observation, and other resource types.
Resources are linked with proper references and submitted as a transaction bundle.
For FHIR servers that don't auto-resolve urn:uuid references, this endpoint will automatically
resolve them via PUT requests after the initial bundle creation.
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
client.tools.create_fhir_resources_multi(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
    provider="medplum",
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

**text:** `str` — Natural language text containing multiple clinical concepts to extract
    
</dd>
</dl>

<dl>
<dd>

**provider:** `str` — FHIR provider ID or name
    
</dd>
</dl>

<dl>
<dd>

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[str]` — FHIR version to use
    
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
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
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

**phenoml_on_behalf_of:** `typing.Optional[str]` 

Optional header for on-behalf-of authentication. Used when making requests on behalf of another user or entity.
Must be in the format: Patient/{uuid} or Practitioner/{uuid}
    
</dd>
</dl>

<dl>
<dd>

**phenoml_fhir_provider:** `typing.Optional[str]` 

Optional header for FHIR provider authentication. Contains credentials in the format {fhir_provider_id}:{oauth2_token}.
Multiple FHIR provider integrations can be provided as comma-separated values.
    
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

## Workflows
<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves all workflow definitions for the authenticated user
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
client.workflows.list(
    verbose=True,
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

**verbose:** `typing.Optional[bool]` — If true, includes full workflow implementation details in workflow_details field
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new workflow definition with graph generation from workflow instructions
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
client.workflows.create(
    verbose=True,
    name="Patient Data Mapping Workflow",
    workflow_instructions="Given diagnosis data, find the patient and create condition record",
    sample_data={
        "patient_last_name": "Rippin",
        "patient_first_name": "Clay",
        "diagnosis_code": "I10",
    },
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
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

**name:** `str` — Human-readable name for the workflow
    
</dd>
</dl>

<dl>
<dd>

**workflow_instructions:** `str` — Natural language instructions that define the workflow logic
    
</dd>
</dl>

<dl>
<dd>

**sample_data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Sample data to use for workflow graph generation
    
</dd>
</dl>

<dl>
<dd>

**fhir_provider_id:** `CreateWorkflowRequestFhirProviderId` — FHIR provider ID(s) - must be valid UUID(s) from existing FHIR providers
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — If true, includes full workflow implementation details in workflow_details field
    
</dd>
</dl>

<dl>
<dd>

**dynamic_generation:** `typing.Optional[bool]` — Enable dynamic lang2fhir calls instead of pre-populated templates
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves a workflow definition by its ID
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
client.workflows.get(
    id="id",
    verbose=True,
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

**id:** `str` — ID of the workflow to retrieve
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — If true, includes full workflow implementation details in workflow_details field
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing workflow definition
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
client.workflows.update(
    id="id",
    verbose=True,
    name="Updated Patient Data Mapping Workflow",
    workflow_instructions="Given diagnosis data, find the patient and create condition record",
    sample_data={
        "patient_last_name": "Smith",
        "patient_first_name": "John",
        "diagnosis_code": "E11",
    },
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
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

**id:** `str` — ID of the workflow to update
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — Human-readable name for the workflow
    
</dd>
</dl>

<dl>
<dd>

**workflow_instructions:** `str` — Natural language instructions that define the workflow logic
    
</dd>
</dl>

<dl>
<dd>

**sample_data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Sample data to use for workflow graph generation
    
</dd>
</dl>

<dl>
<dd>

**fhir_provider_id:** `UpdateWorkflowRequestFhirProviderId` — FHIR provider ID(s) - must be valid UUID(s) from existing FHIR providers
    
</dd>
</dl>

<dl>
<dd>

**verbose:** `typing.Optional[bool]` — If true, includes full workflow implementation details in workflow_details field
    
</dd>
</dl>

<dl>
<dd>

**dynamic_generation:** `typing.Optional[bool]` — Enable dynamic lang2fhir calls instead of pre-populated templates
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a workflow definition by its ID
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
client.workflows.delete(
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

**id:** `str` — ID of the workflow to delete
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">execute</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Executes a workflow with provided input data and returns results
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
client.workflows.execute(
    id="id",
    input_data={
        "patient_last_name": "Johnson",
        "patient_first_name": "Mary",
        "diagnosis_code": "M79.3",
        "encounter_date": "2024-01-15",
    },
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

**id:** `str` — ID of the workflow to execute
    
</dd>
</dl>

<dl>
<dd>

**input_data:** `typing.Dict[str, typing.Optional[typing.Any]]` — Input data for workflow execution
    
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

