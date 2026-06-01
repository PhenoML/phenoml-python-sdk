# Reference
## Agent
<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">create</a>(...) -> AgentResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.create(
    name="Medical Assistant",
    description="An AI assistant for medical information processing",
    prompts=[
        "prompt_123"
    ],
    tags=[
        "medical",
        "fhir"
    ],
    provider="7002b0b4-8d09-445a-bf65-0fafdaf26c35",
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

**request:** `AgentCreateRequest` 
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">list</a>(...) -> AgentListResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">get</a>(...) -> AgentResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">update</a>(...) -> AgentResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.update(
    id="id",
    name="Medical Assistant",
    description="Updated description for the medical assistant",
    prompts=[
        "prompt_123"
    ],
    tags=[
        "medical",
        "fhir",
        "updated"
    ],
    provider="7002b0b4-8d09-445a-bf65-0fafdaf26c35",
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

**request:** `AgentCreateRequest` 
    
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">delete</a>(...) -> AgentDeleteResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.<a href="src/phenoml/agent/client.py">patch</a>(...) -> AgentResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.agent import JsonPatchOperation

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.patch(
    id="id",
    request=[
        JsonPatchOperation(
            op="replace",
            path="/description",
            value="patched description",
        ),
        JsonPatchOperation(
            op="add",
            path="/tags/-",
            value="updated",
        )
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

## Chat
<details><summary><code>client.agent.chat.<a href="src/phenoml/agent/chat/client.py">send</a>(...) -> AgentChatResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to an agent and receive a JSON response.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.chat.send(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    message="What is the patient\'s current condition?",
    session_id="session-abc123",
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

**enhanced_reasoning:** `typing.Optional[bool]` — Enable enhanced reasoning capabilities. Increases latency but improves response quality and reliability.
    
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

<details><summary><code>client.agent.chat.<a href="src/phenoml/agent/chat/client.py">stream</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Send a message to an agent and receive the response as a Server-Sent Events
(SSE) stream. Events include message_start, content_delta, tool_use,
tool_result, message_end, and error.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.chat.stream(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    message="What is the patient\'s current condition?",
    session_id="session-abc123",
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

**enhanced_reasoning:** `typing.Optional[bool]` — Enable enhanced reasoning capabilities. Increases latency but improves response quality and reliability.
    
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

<details><summary><code>client.agent.chat.<a href="src/phenoml/agent/chat/client.py">list_messages</a>(...) -> ListMessagesResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.chat.list_messages(
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

**role:** `typing.Optional[ListMessagesRequestRole]` 

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

**order:** `typing.Optional[ListMessagesRequestOrder]` — Order of messages
    
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

## Prompts
<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">create</a>(...) -> AgentPromptsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.prompts.create(
    name="Medical Assistant System Prompt",
    description="System prompt for medical assistant agent",
    content="You are a helpful medical assistant specialized in FHIR data processing.",
    is_default=False,
    tags=[
        "medical",
        "system"
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

**tags:** `typing.Optional[typing.List[str]]` — Tags for categorizing the prompt
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">list</a>() -> PromptListResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">get</a>(...) -> AgentPromptsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">update</a>(...) -> AgentPromptsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.prompts.update(
    id="id",
    name="Medical Assistant System Prompt",
    description="Updated system prompt",
    content="You are a helpful medical assistant. Always cite ICD-10 codes when discussing diagnoses.",
    is_default=False,
    tags=[
        "medical",
        "system",
        "updated"
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

**tags:** `typing.Optional[typing.List[str]]` — Tags for categorizing the prompt
    
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">delete</a>(...) -> PromptDeleteResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.agent.prompts.<a href="src/phenoml/agent/prompts/client.py">patch</a>(...) -> AgentPromptsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.agent import JsonPatchOperation

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.agent.prompts.patch(
    id="id",
    request=[
        JsonPatchOperation(
            op="replace",
            path="/content",
            value="Updated prompt content.",
        )
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

## Authtoken
<details><summary><code>client.authtoken.<a href="src/phenoml/authtoken/client.py">get_token</a>(...) -> TokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

OAuth 2.0 client credentials token endpoint (RFC 6749 §4.4).
Accepts client_id and client_secret in the request body (JSON or
form-encoded) or via Basic Auth header (RFC 6749 §2.3.1), and
returns an access token with expiration information.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.authtoken.get_token(
    client_id="your_client_id",
    client_secret="your_client_secret",
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

**grant_type:** `typing.Optional[str]` — Must be "client_credentials" if provided
    
</dd>
</dl>

<dl>
<dd>

**client_id:** `typing.Optional[str]` — The client ID (credential username)
    
</dd>
</dl>

<dl>
<dd>

**client_secret:** `typing.Optional[str]` — The client secret (credential password)
    
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
<details><summary><code>client.cohort.<a href="src/phenoml/cohort/client.py">analyze</a>(...) -> CohortResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

## Code Systems
<details><summary><code>client.construe.code_systems.<a href="src/phenoml/construe/code_systems/client.py">upload</a>(...) -> UploadResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.construe import CodeResponse

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.code_systems.upload(
    name="CUSTOM_CODES",
    version="1.0",
    format="json",
    codes=[
        CodeResponse(
            code="X001",
            description="Example custom code 1",
        ),
        CodeResponse(
            code="X002",
            description="Example custom code 2",
        )
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

**codes:** `typing.Optional[typing.List[CodeResponse]]` 

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

<details><summary><code>client.construe.code_systems.<a href="src/phenoml/construe/code_systems/client.py">list</a>() -> ListCodeSystemsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.code_systems.list()

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

<details><summary><code>client.construe.code_systems.<a href="src/phenoml/construe/code_systems/client.py">find</a>(...) -> GetCodeSystemDetailResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.code_systems.find(
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

<details><summary><code>client.construe.code_systems.<a href="src/phenoml/construe/code_systems/client.py">delete</a>(...) -> DeleteCodeSystemResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.code_systems.delete(
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

<details><summary><code>client.construe.code_systems.<a href="src/phenoml/construe/code_systems/client.py">export</a>(...) -> ExportCodeSystemResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.code_systems.export(
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

## Construe
<details><summary><code>client.construe.<a href="src/phenoml/construe/client.py">submit_feedback</a>(...) -> FeedbackResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submits user feedback on results from the Construe extraction endpoint.
Feedback includes the full extraction result received and the result the user expected.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.construe import ExtractCodesResult, ExtractRequestSystem, ExtractedCodeResult

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.submit_feedback(
    text="Patient has type 2 diabetes with hyperglycemia",
    received_result=ExtractCodesResult(
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="2025",
        ),
        codes=[
            ExtractedCodeResult(
                code="E11.9",
                description="Type 2 diabetes mellitus without complications",
                valid=True,
            )
        ],
    ),
    expected_result=ExtractCodesResult(
        system=ExtractRequestSystem(
            name="ICD-10-CM",
            version="2025",
        ),
        codes=[
            ExtractedCodeResult(
                code="E11.65",
                description="Type 2 diabetes mellitus with hyperglycemia",
                valid=True,
            )
        ],
    ),
    detail="Expected code E11.65 because the text mentions hyperglycemia",
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

**text:** `str` — The natural language text that was used for code extraction
    
</dd>
</dl>

<dl>
<dd>

**received_result:** `ExtractCodesResult` 
    
</dd>
</dl>

<dl>
<dd>

**expected_result:** `ExtractCodesResult` 
    
</dd>
</dl>

<dl>
<dd>

**detail:** `typing.Optional[str]` — Optional details explaining the feedback
    
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

## Codes
<details><summary><code>client.construe.codes.<a href="src/phenoml/construe/codes/client.py">extract</a>(...) -> ExtractCodesResult</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.construe import ExtractRequestSystem

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.codes.extract(
    text="Patient is a 14-year-old female, previously healthy, who is here for evaluation of abnormal renal ultrasound with atrophic right kidney.",
    system=ExtractRequestSystem(
        name="ICD-10-CM",
        version="2025",
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

<details><summary><code>client.construe.codes.<a href="src/phenoml/construe/codes/client.py">list</a>(...) -> ListCodesResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.codes.list(
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

<details><summary><code>client.construe.codes.<a href="src/phenoml/construe/codes/client.py">lookup</a>(...) -> GetCodeResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.codes.lookup(
    codesystem="ICD-10-CM",
    code_id="E1165",
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

**code_id:** `str` 

The code identifier. ICD-10-CM codes are stored without their
cosmetic dot (use "E1165", not "E11.65").
    
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

<details><summary><code>client.construe.codes.<a href="src/phenoml/construe/codes/client.py">search_semantic</a>(...) -> SemanticSearchResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.codes.search_semantic(
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

<details><summary><code>client.construe.codes.<a href="src/phenoml/construe/codes/client.py">search_text</a>(...) -> TextSearchResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.construe.codes.search_text(
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
<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">search</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves FHIR resources from the specified provider. Supports both individual resource retrieval (e.g. `Patient/123` via the path) and search operations.

FHIR search parameters are passed through to the upstream server verbatim as native query-string parameters; this proxy does not model, validate, or transform them. Append standard FHIR search parameters directly to the request URL. Supported parameters include:
- Resource-specific search parameters (e.g. `name` for Patient, `status` for Observation)
- Common search parameters (`_id`, `_lastUpdated`, `_tag`, `_profile`, `_security`, `_text`, `_content`, `_filter`)
- Result parameters (`_count`, `_offset`, `_sort`, `_include`, `_revinclude`, `_summary`, `_elements`)
- Search prefixes for dates, numbers, and quantities (`eq`, `ne`, `gt`, `ge`, `lt`, `le`, `sa`, `eb`, `ap`)

Examples:
- `Patient?name=John%20Doe&_count=10&_sort=family`
- `Observation?patient=Patient/123&date=ge2023-01-01&category=vital-signs&_sort=-date`

When using a generated SDK, supply these via the client's request-level query-parameter option (the SDK escape hatch) rather than a typed argument.

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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">create</a>(...) -> typing.Any</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir.create(
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    request={"resourceType": "Patient"},
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

**request:** `typing.Any` 
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">upsert</a>(...) -> typing.Any</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir.upsert(
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    request={"resourceType": "Patient", "id": "123"},
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

**request:** `typing.Any` 
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">delete</a>(...) -> typing.Any</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">patch</a>(...) -> typing.Any</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Partially updates a FHIR resource on the specified provider.

Two body formats are supported, selected by request content type:
- `application/json-patch+json` — an array of JSON Patch operations as defined in RFC 6902. Each operation specifies:
  - `op`: The operation type (add, remove, replace, move, copy, test)
  - `path`: JSON Pointer to the target location in the resource
  - `value`: The value to use (required for add, replace, and test operations)
- `application/fhir+json` — a partial FHIR resource for merge-patch semantics.

**Note:** This proxy currently forwards the request body to the upstream FHIR server with `Content-Type: application/fhir+json` regardless of the declared request content type. JSON Patch (RFC 6902) therefore only succeeds against upstream servers that accept patch arrays under `application/fhir+json`; servers that strictly enforce patch media types may reject or misinterpret it. Support for either format ultimately depends on the upstream FHIR server.

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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.fhir import PatchRequestBodyItem

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir.patch(
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    fhir_path="Patient",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    request=[
        PatchRequestBodyItem(
            op="replace",
            path="/name/0/family",
            value="NewFamilyName",
        )
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

**request:** `typing.List[PatchRequestBodyItem]` — Array of JSON Patch operations following RFC 6902
    
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

<details><summary><code>client.fhir.<a href="src/phenoml/fhir/client.py">execute_bundle</a>(...) -> typing.Any</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir.execute_bundle(
    fhir_provider_id="550e8400-e29b-41d4-a716-446655440000",
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    request={"resourceType": "Bundle", "type": "transaction", "entry": [{"request": {"method": "POST", "url": "Patient"}, "resource": {"resourceType": "Patient", "name": [{"family": "Doe", "given": ["John"]}]}}, {"request": {"method": "POST", "url": "Observation"}, "resource": {"resourceType": "Observation", "status": "final", "subject": {"reference": "Patient/123"}}}]},
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

**request:** `typing.Any` 
    
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

## FhirProvider
<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">create</a>(...) -> FhirProviderResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.fhir_provider import FhirProviderCreateRequestAuth_ClientSecret

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir_provider.create(
    name="Epic Sandbox",
    description="Epic sandbox environment for testing",
    provider="epic",
    base_url="https://fhir.epic.com/interconnect-fhir-oauth/api/FHIR/R4",
    auth=FhirProviderCreateRequestAuth_ClientSecret(
        client_id="your-client-id",
        client_secret="your-client-secret",
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

**base_url:** `str` — Base URL of the FHIR server
    
</dd>
</dl>

<dl>
<dd>

**auth:** `FhirProviderCreateRequestAuth` 
    
</dd>
</dl>

<dl>
<dd>

**description:** `typing.Optional[str]` — Optional description of the FHIR provider
    
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">list</a>() -> FhirProviderListResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">get</a>(...) -> FhirProviderResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.fhir_provider.<a href="src/phenoml/fhir_provider/client.py">delete</a>(...) -> DeleteResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deletes a FHIR provider.

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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

## Auth Config
<details><summary><code>client.fhir_provider.auth_config.<a href="src/phenoml/fhir_provider/auth_config/client.py">add</a>(...) -> FhirProviderResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment
from phenoml.fhir_provider import FhirProviderAddAuthConfigRequest_ClientSecret

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir_provider.auth_config.add(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    request=FhirProviderAddAuthConfigRequest_ClientSecret(
        client_id="your-client-id",
        client_secret="your-client-secret",
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

**fhir_provider_id:** `str` — ID of the FHIR provider to add auth config to
    
</dd>
</dl>

<dl>
<dd>

**request:** `FhirProviderAddAuthConfigRequest` 
    
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

<details><summary><code>client.fhir_provider.auth_config.<a href="src/phenoml/fhir_provider/auth_config/client.py">set_active</a>(...) -> FhirProviderResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir_provider.auth_config.set_active(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    auth_config_id="auth-config-456",
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

<details><summary><code>client.fhir_provider.auth_config.<a href="src/phenoml/fhir_provider/auth_config/client.py">remove</a>(...) -> RemoveResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.fhir_provider.auth_config.remove(
    fhir_provider_id="1716d214-de93-43a4-aa6b-a878d864e2ad",
    auth_config_id="auth-config-456",
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
<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">create</a>(...) -> FhirResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Converts natural language text into a structured FHIR resource.

**Patient identifier handling.** When generating a `patient` (or `patient-canvas`) resource, US Core requires `Patient.identifier` (a business identifier such as an MRN). When the source text contains an identifier, it is extracted with an appropriate URI system. When the source text does not contain a detectable identifier, a synthetic one is generated with `system: "urn:phenoml:lang2fhir-generated-id"` and a UUID `value` so the resource remains FHIR-valid and US Core conformant. Callers who need a tenant-specific namespace should rewrite the synthetic system after extraction.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.lang2fhir.create(
    version="R4",
    resource="condition-encounter-diagnosis",
    text="Patient has severe persistent asthma with acute exacerbation",
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">create_multi</a>(...) -> CreateMultiResponse</code></summary>
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

**Patient identifier handling.** US Core requires `Patient.identifier` (a business identifier such as an MRN). When the source text contains an identifier, it is extracted with an appropriate URI system. When the source text does not contain a detectable identifier, a synthetic one is generated with `system: "urn:phenoml:lang2fhir-generated-id"` and a UUID `value` so the bundle remains FHIR-valid and US Core conformant. Callers who need a tenant-specific namespace should rewrite the synthetic system after extraction.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.lang2fhir.create_multi(
    text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily. Blood pressure 140/90.",
    version="R4",
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

**implementation_guide:** `typing.Optional[str]` — Custom Implementation Guide name. When specified, profiles from this IG are included alongside US Core profiles during resource detection. US Core is always the base layer; custom IG profiles are additive.
    
</dd>
</dl>

<dl>
<dd>

**detection_effort:** `typing.Optional[CreateMultiRequestDetectionEffort]` — Detection effort. 'standard' runs detection once, 'deep' runs detection multiple times for higher recall.
    
</dd>
</dl>

<dl>
<dd>

**validation_method:** `typing.Optional[CreateMultiRequestValidationMethod]` — FHIR validation method to apply to the generated bundle. 'none' skips validation (default). 'check' runs the bundle through a FHIR structure validator and includes the results in the response. 'fix' runs validation and attempts to auto-correct errors using an LLM (up to 3 validation passes). The response includes results from each pass. Warning: 'fix' can significantly increase latency due to multiple LLM and validation round-trips.
    
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">search</a>(...) -> SearchResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">upload_profile</a>(...) -> UploadProfileResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.lang2fhir.upload_profile(
    profile="eyJyZXNvdXJjZVR5cGUiOiJTdHJ1Y3R1cmVEZWZpbml0aW9uIiwiaWQiOiJjdXN0b20tcGF0aWVudCIsInVybCI6Imh0dHA6Ly9waGVub21sLmNvbS9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vY3VzdG9tLXBhdGllbnQiLCJuYW1lIjoiQ3VzdG9tUGF0aWVudCIsInN0YXR1cyI6ImFjdGl2ZSIsImZoaXJWZXJzaW9uIjoiNC4wLjEiLCJraW5kIjoicmVzb3VyY2UiLCJhYnN0cmFjdCI6ZmFsc2UsInR5cGUiOiJQYXRpZW50IiwiYmFzZURlZmluaXRpb24iOiJodHRwOi8vaGw3Lm9yZy9maGlyL1N0cnVjdHVyZURlZmluaXRpb24vUGF0aWVudCIsImRlcml2YXRpb24iOiJjb25zdHJhaW50Iiwic25hcHNob3QiOnsiZWxlbWVudCI6W3siaWQiOiJQYXRpZW50IiwicGF0aCI6IlBhdGllbnQiLCJtaW4iOjAsIm1heCI6IioifSx7ImlkIjoiUGF0aWVudC5uYW1lIiwicGF0aCI6IlBhdGllbnQubmFtZSIsIm1pbiI6MSwibWF4IjoiKiJ9XX19Cg==",
    implementation_guide="acme-cardiology",
    profile_context="When clinical text describes cardiology-specific findings, prefer this profile over the generic US Core Condition.",
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

**implementation_guide:** `typing.Optional[str]` — Implementation Guide name to group this profile under. Defaults to "custom" if omitted. Cannot be "us_core" (reserved). Use this to organize custom profiles into named IGs that can be referenced when calling create/multi or document/multi endpoints.
    
</dd>
</dl>

<dl>
<dd>

**profile_context:** `typing.Optional[str]` — Natural language context that helps the LLM select the right profiles from this implementation guide during resource detection. For example, "When the text mentions phenotypic features or abnormalities, prefer the hpo-observation profile over Condition." This is stored as IG-level metadata and injected into the LLM prompt. Max 2000 characters. Providing this field on any upload will update the context for the entire IG (last write wins).
    
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">document</a>(...) -> FhirResource</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts text from a document (PDF or image) and converts it into a structured FHIR resource.

**Patient identifier handling.** When generating a `patient` (or `patient-canvas`) resource, US Core requires `Patient.identifier` (a business identifier such as an MRN). When the source text contains an identifier, it is extracted with an appropriate URI system. When the source text does not contain a detectable identifier, a synthetic one is generated with `system: "urn:phenoml:lang2fhir-generated-id"` and a UUID `value` so the resource remains FHIR-valid and US Core conformant. Callers who need a tenant-specific namespace should rewrite the synthetic system after extraction.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.lang2fhir.document(
    version="R4",
    resource="questionnaire",
    content="JVBERi0xLjQKJeLjz9MK...(base64-encoded PDF or image bytes)",
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

**resource:** `str` — Type of FHIR resource to create. Accepts any FHIR resource type or US Core profile name.
    
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

**config:** `typing.Optional[DocumentConfig]` 
    
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

<details><summary><code>client.lang2fhir.<a href="src/phenoml/lang2fhir/client.py">document_multi</a>(...) -> DocumentMultiResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Extracts text from a document (PDF or image) and converts it into multiple FHIR resources,
returned as a transaction Bundle. Combines document text extraction with multi-resource detection.
Automatically detects Patient, Condition, MedicationRequest, Observation, and other resource types.
Resources are linked with proper references (e.g., Conditions reference the Patient).

**Patient identifier handling.** US Core requires `Patient.identifier` (a business identifier such as an MRN). When the source text contains an identifier, it is extracted with an appropriate URI system. When the source text does not contain a detectable identifier, a synthetic one is generated with `system: "urn:phenoml:lang2fhir-generated-id"` and a UUID `value` so the bundle remains FHIR-valid and US Core conformant. Callers who need a tenant-specific namespace should rewrite the synthetic system after extraction.
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.lang2fhir.document_multi(
    version="R4",
    content="JVBERi0xLjQKJeLjz9MK...(base64-encoded PDF or image bytes)",
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

**version:** `str` — FHIR version to use
    
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

**provider:** `typing.Optional[str]` — Optional FHIR provider name for provider-specific profiles
    
</dd>
</dl>

<dl>
<dd>

**implementation_guide:** `typing.Optional[str]` — Custom Implementation Guide name. When specified, profiles from this IG are included alongside US Core profiles during resource detection. US Core is always the base layer; custom IG profiles are additive.
    
</dd>
</dl>

<dl>
<dd>

**detection_effort:** `typing.Optional[DocumentMultiRequestDetectionEffort]` — Detection effort. 'standard' runs detection once, 'deep' runs detection multiple times for higher recall.
    
</dd>
</dl>

<dl>
<dd>

**validation_method:** `typing.Optional[DocumentMultiRequestValidationMethod]` — FHIR validation method to apply to the generated bundle. 'none' skips validation (default). 'check' runs the bundle through a FHIR structure validator and includes the results in the response. 'fix' runs validation and attempts to auto-correct errors using an LLM (up to 3 validation passes). The response includes results from each pass. Warning: 'fix' can significantly increase latency due to multiple LLM and validation round-trips.
    
</dd>
</dl>

<dl>
<dd>

**config:** `typing.Optional[DocumentConfig]` 
    
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

## Templates
<details><summary><code>client.summary.templates.<a href="src/phenoml/summary/templates/client.py">list</a>() -> ListResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.templates.list()

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

<details><summary><code>client.summary.templates.<a href="src/phenoml/summary/templates/client.py">create</a>(...) -> CreateSummaryTemplateResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.templates.create(
    name="Discharge Summary",
    example_summary="Patient John Doe, age 45, was admitted on 2024-01-10 with Type 2 Diabetes. Discharged on 2024-01-15 with Metformin 500mg BID.",
    target_resources=[
        "Patient",
        "Condition",
        "MedicationRequest"
    ],
    mode="narrative",
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

**target_resources:** `typing.List[str]` — List of target FHIR resources
    
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

**example_fhir_data:** `typing.Optional[typing.Dict[str, typing.Any]]` — Optional example FHIR data that corresponds to the example summary
    
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

<details><summary><code>client.summary.templates.<a href="src/phenoml/summary/templates/client.py">get</a>(...) -> GetResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.templates.get(
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

<details><summary><code>client.summary.templates.<a href="src/phenoml/summary/templates/client.py">update</a>(...) -> UpdateResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.templates.update(
    id="id",
    name="Discharge Summary",
    template="Patient {{Patient.name[0].text}} was discharged on {{Encounter[0].period.end}} with {{MedicationRequest[0].medicationCodeableConcept.coding[0].display}} {{MedicationRequest[0].dosageInstruction[0].text}}.",
    target_resources=[
        "Patient",
        "Encounter",
        "MedicationRequest"
    ],
    mode="narrative",
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

**target_resources:** `typing.List[str]` 
    
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

<details><summary><code>client.summary.templates.<a href="src/phenoml/summary/templates/client.py">delete</a>(...) -> DeleteResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.templates.delete(
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

## Summary
<details><summary><code>client.summary.<a href="src/phenoml/summary/client.py">create</a>(...) -> CreateSummaryResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.summary.create(
    mode="narrative",
    template_id="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    fhir_resources={
        "resourceType": "Bundle",
        "type": "collection",
        "entry": [{"resource": {"resourceType": "Patient", "name": [{"given": ["John"], "family": "Doe"}], "gender": "male", "birthDate": "1979-03-15"}}, {"resource": {"resourceType": "Condition", "code": {"text": "Type 2 Diabetes Mellitus"}, "onsetDateTime": "2024-01-15"}}]
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

**fhir_resources:** `typing.Dict[str, typing.Any]` 

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
<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">create_fhir_resource</a>(...) -> Lang2FhirAndCreateResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.create_fhir_resource(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    resource="condition-encounter-diagnosis",
    text="Patient has severe persistent asthma with acute exacerbation",
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">create_fhir_resources_multi</a>(...) -> Lang2FhirAndCreateMultiResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.create_fhir_resources_multi(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    text="John Smith, 45-year-old male, diagnosed with Type 2 Diabetes. Prescribed Metformin 500mg twice daily.",
    version="R4",
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">search_fhir_resources</a>(...) -> Lang2FhirAndSearchResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.search_fhir_resources(
    phenoml_on_behalf_of="Patient/550e8400-e29b-41d4-a716-446655440000",
    phenoml_fhir_provider="550e8400-e29b-41d4-a716-446655440000:eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c...",
    text="Find all appointments for patient John Doe next week",
    count=10,
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

<details><summary><code>client.tools.<a href="src/phenoml/tools/client.py">analyze_cohort</a>(...) -> CohortResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

## MCP Servers
<details><summary><code>client.tools.mcp_servers.<a href="src/phenoml/tools/mcp_servers/client.py">create</a>(...) -> McpServerResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_servers.create(
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

<details><summary><code>client.tools.mcp_servers.<a href="src/phenoml/tools/mcp_servers/client.py">list</a>() -> McpServerResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_servers.list()

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

<details><summary><code>client.tools.mcp_servers.<a href="src/phenoml/tools/mcp_servers/client.py">get</a>(...) -> McpServerResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_servers.get(
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

<details><summary><code>client.tools.mcp_servers.<a href="src/phenoml/tools/mcp_servers/client.py">delete</a>(...) -> McpServerResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_servers.delete(
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

## MCP Tools
<details><summary><code>client.tools.mcp_tools.<a href="src/phenoml/tools/mcp_tools/client.py">list</a>(...) -> McpServerToolResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_tools.list(
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

<details><summary><code>client.tools.mcp_tools.<a href="src/phenoml/tools/mcp_tools/client.py">get</a>(...) -> McpServerToolResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_tools.get(
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

<details><summary><code>client.tools.mcp_tools.<a href="src/phenoml/tools/mcp_tools/client.py">delete</a>(...) -> McpServerToolResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.tools.mcp_tools.delete(
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

## Workflows
<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">list</a>(...) -> ListWorkflowsResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">create</a>(...) -> CreateWorkflowResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.workflows.create(
    verbose=True,
    name="Patient Data Mapping Workflow",
    workflow_instructions="Given diagnosis data, find the patient and create a condition record linked to their encounter",
    sample_data={
        "patient_last_name": "Rippin",
        "patient_first_name": "Clay",
        "diagnosis_code": "I10",
        "encounter_date": "2024-01-15"
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

**sample_data:** `typing.Dict[str, typing.Any]` — Sample data to use for workflow graph generation
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">get</a>(...) -> GetResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">update</a>(...) -> UpdateResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.workflows.update(
    id="id",
    verbose=True,
    name="Patient Data Mapping Workflow (v2)",
    workflow_instructions="Given diagnosis data, find the patient and create a condition record linked to their encounter",
    sample_data={
        "patient_last_name": "Rippin",
        "patient_first_name": "Clay",
        "diagnosis_code": "I10",
        "encounter_date": "2024-01-15"
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

**sample_data:** `typing.Dict[str, typing.Any]` — Sample data to use for workflow graph generation
    
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">delete</a>(...) -> DeleteResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
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

<details><summary><code>client.workflows.<a href="src/phenoml/workflows/client.py">execute</a>(...) -> ExecuteWorkflowResponse</code></summary>
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
from phenoml import PhenomlClient
from phenoml.environment import PhenomlClientEnvironment

client = PhenomlClient(
    client_id="<clientId>",
    client_secret="<clientSecret>",
    environment=PhenomlClientEnvironment.DEFAULT,
)

client.workflows.execute(
    id="7a8b9c0d-1234-5678-abcd-ef9876543210",
    input_data={
        "patient_last_name": "Johnson",
        "patient_first_name": "Mary",
        "diagnosis_code": "M79.3",
        "encounter_date": "2024-03-20"
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

**input_data:** `typing.Dict[str, typing.Any]` — Input data for workflow execution
    
</dd>
</dl>

<dl>
<dd>

**preview:** `typing.Optional[bool]` — If true, create operations return mock resources instead of persisting to the FHIR server
    
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

