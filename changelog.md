## 7.3.0 - 2026-03-03
* feat: add document multi-resource extraction endpoint
* Add comprehensive support for extracting multiple FHIR resources from documents through a new API endpoint. This enhancement combines document text extraction with multi-resource detection capabilities.
* Key changes:
* Add extract_multiple_fhir_resources_from_a_document method for both sync and async clients
* Implement new UnprocessableEntityError (422) for handling validation errors
* Add comprehensive documentation and examples for the new endpoint
* Support automatic detection of Patient, Condition, MedicationRequest, Observation resources
* Include proper resource linking with references between related resources
* 🌿 Generated with Fern

## 7.2.0 - 2026-03-03
* feat: add feedback submission for extraction results
* Add new functionality to submit user feedback on Construe extraction endpoint results. This enables users to provide feedback comparing actual extraction results with expected outcomes to improve the service.
* Key changes:
* Add submit_feedback_on_extraction_results method to both sync and async clients
* Create FeedbackResponse type to handle feedback submission responses
* Add comprehensive documentation and usage examples for the new endpoint
* Include proper error handling for all standard HTTP error responses
* 🌿 Generated with Fern

## 7.1.0 - 2026-03-02
* refactor: replace DocumentRequestResource with generic string type
* Removes the restrictive DocumentRequestResource enum type and replaces it with a generic string type to support all FHIR resource types and US Core profile names. This improves flexibility by allowing the API to accept any valid FHIR resource type instead of being limited to just questionnaire and questionnaireresponse.
* Key changes:
* Remove DocumentRequestResource type definition and imports
* Update document() method signatures to accept `str` instead of `DocumentRequestResource`
* Update documentation to reflect expanded resource type support
* Clean up all references across client, raw client, and types modules
* 🌿 Generated with Fern

## 7.0.0 - 2026-02-26
* feat: refactor FHIR provider authentication to use structured auth types
* Refactor FHIR provider API from individual auth parameters to structured auth
* configuration objects, improving type safety and developer experience. This
* change replaces separate auth_method, client_id, client_secret and other
* parameters with unified auth objects that encapsulate auth-specific fields.
* Key changes:
* Replace individual auth parameters with FhirProviderCreateRequestAuth union type
* Replace add_auth_config parameters with FhirProviderAddAuthConfigRequest union type
* Add new auth type classes: ClientSecretAuth, JwtAuth, GoogleHealthcareAuth, etc.
* Update examples to use new structured auth approach (e.g., FhirProviderCreateRequestAuth_Jwt)
* Add servicerequest resource type support
* Update CLI version from 3.86.0 to 3.88.4
* Update certifi dependency from 2026.1.4 to 2026.2.25
* 🌿 Generated with Fern

## 6.2.0 - 2026-02-25
* feat: add servicerequest resource type support
* Extend the CreateRequestResource union type to include "servicerequest"
* as a supported resource type for the lang2fhir service. This enhancement
* provides additional FHIR resource creation capabilities for service
* request workflows.
* Key changes:
* Add "servicerequest" to CreateRequestResource union type
* Update CLI version from 3.85.2 to 3.86.0 in metadata
* Maintain backward compatibility with existing resource types
* 🌿 Generated with Fern

## 6.1.0 - 2026-02-24
* feat: add client_id parameter to FHIR provider auth configuration
* Enhance FHIR provider authentication by adding optional client_id parameter to auth configurations. This provides more granular control over OAuth authentication at the individual configuration level rather than only at the provider template level.
* The client_id parameter is now available in the add_auth_config method for both sync and async FHIR provider clients. When set at the auth configuration level, it takes precedence over the provider-level client_id for better flexibility in multi-tenant scenarios.
* Key changes:
* Add optional client_id parameter to add_auth_config methods in both sync and async clients
* Include client_id in FhirProviderAuthConfig type with proper documentation
* Update documentation to clarify OAuth client ID requirements for different auth methods
* Mark provider-level client_id as deprecated in favor of auth-config-level setting
* Maintain backward compatibility with existing provider configurations
* 🌿 Generated with Fern

## 6.0.0 - 2026-02-23
* refactor: update delete behavior and remove is_active fields
* Updates FHIR provider deletion to use hard deletes instead of soft deletes. This change simplifies the data model by removing the is_active tracking field and aligning the behavior with actual deletion operations.
* Key changes:
* Update documentation to reflect hard delete behavior for FHIR providers
* Remove is_active field from FhirProviderSandboxInfo model
* Remove is_active field from FhirProviderTemplate model
* Remove is_active field from McpServerResponseData model
* Remove is_active field from McpServerToolResponseData model
* 🌿 Generated with Fern

## 5.6.0 - 2026-02-23
* feat: refactor authentication configuration with simplified role system
* Refactor FHIR provider authentication configuration by restructuring parameters, improving documentation clarity, and simplifying the role system. The changes enhance usability by making parameter usage more explicit and reducing complexity in role definitions.
* Key changes:
* Add credential_expiry parameter to method signatures for JWT authentication
* Update client_id description to specify required auth methods (jwt, client_secret, on_behalf_of)
* Enhance scopes parameter documentation with auth method restrictions and better guidance
* Simplify Role type from multiple specific literals to admin/read/write options
* Improve credential_expiry documentation with default behavior clarification
* 🌿 Generated with Fern

## 5.5.0 - 2026-02-20
* feat: add phenostore as an option for FHIR Provider
* Add "phenostore" as a new supported provider in the FHIR Provider type, expanding the set of available healthcare data integrations.
* Key changes:
* Add "phenostore" to the Provider union type alongside existing providers
* 🌿 Generated with Fern

## 5.4.0 - 2026-02-20
* feat: add streaming chat functionality to agent client
* Add support for Server-Sent Events (SSE) streaming in agent chat, allowing real-time response streaming. This enhancement provides a new stream_chat method alongside the existing chat method for different use cases.
* Key changes:
* Add stream_chat method with SSE support for both sync and async clients
* Introduce AgentChatStreamEvent and AgentChatStreamEventType for streaming response handling
* Update CI workflow to simplify job dependencies and remove auto-tagging
* Update Fern CLI version from 3.74.1 to 3.76.0
* Improve chat method documentation to clarify JSON vs streaming response types
* 🌿 Generated with Fern

## 5.3.0 - 2026-02-17
* feat: add enhanced reasoning parameter and update generator version
* Add support for enhanced reasoning capabilities across agent chat methods in both sync and async clients. This new optional parameter enables improved response quality and reliability with increased latency.
* Key changes:
* Add enhanced_reasoning optional boolean parameter to agent chat methods
* Update generator version from 4.35.3 to 4.35.4 in metadata
* Remove User-Agent header from client wrapper
* Fix GitHub Actions workflow formatting and missing job name
* Update documentation to describe enhanced reasoning functionality
* 🌿 Generated with Fern

## 5.2.1 - 2026-02-13
* fix: tighten type annotations and improve Pydantic v2 compatibility
* Simplify error body types from Optional[Any] to Any across all error constructors
* Tighten dict value types from Dict[str, Optional[Any]] to Dict[str, Any] in workflow and tool parameters
* Fix Pydantic v2 root validation to consistently use model_validator(mode="before")
* Update Poetry build configuration for better compatibility

## 5.2.0 - 2026-02-13
* refactor: update dynamic import system and add SSE support
* Refactor the dynamic import mechanism across all modules to support module-level imports and add comprehensive Server-Sent Events (SSE) support for real-time streaming capabilities.
* Key changes:
* Update __getattr__ functions to handle module-level imports when module_name matches attribute pattern
* Fix incorrect import paths for submodules (prompts, auth, mcp_server, tools)
* Add complete SSE implementation with EventSource, decoders, and connection utilities
* Fix Pydantic serialization to use dict() instead of deprecated model_dump()
* Remove redundant import in test file
* 🌿 Generated with Fern

## 5.1.0 - 2026-02-13
* refactor: switch to lazy imports and deferred sub-client initialization
* All module __init__.py files now use dynamic imports via __getattr__ to reduce startup overhead.
* Sub-clients are lazily instantiated on first access instead of eagerly in __init__.
* Adds force_multipart and http_response core utilities.

## 5.0.0 - 2026-02-13
* refactor: simplify code upload API and improve async processing
* Refactored the construe code system upload functionality to improve API consistency
* and enhance asynchronous processing. The upload endpoint now returns 202 immediately
* for async processing instead of synchronous response, improving user experience for
* large code system uploads.
* Key changes:
* Remove complex union types for upload requests, flatten parameters into direct method arguments
* Change upload behavior to always process asynchronously with 202 response
* Add new error handling for 404 Not Found, 503 Service Unavailable, and 504 Gateway Timeout
* Remove user_id fields from various template models to simplify data structures
* Update documentation to reflect async processing workflow with status polling
* Replace UploadRequest union types with simpler UploadRequestFormat enum
* Rename rationale field to reason in ExtractedCodeResult for consistency
* Add name and version fields to upload response for better tracking
* 🌿 Generated with Fern

## 4.1.0 - 2026-02-09
* feat: add export_custom_code_system method to construe client
* This change introduces a new feature to export custom code systems as JSON files compatible with the upload format. The exported files can be re-uploaded directly via the POST /construe/upload endpoint, enabling better code system management and portability.
* Key changes:
* Add export_custom_code_system method to both sync and async ConstrueClient classes
* Implement corresponding raw client methods with comprehensive error handling
* Create new ExportCodeSystemResponse type for structured export data
* Update module imports and documentation with usage examples
* Remove redundant 403 error handling from FHIR provider endpoints
* 🌿 Generated with Fern

## 4.0.0 - 2026-02-08
* feat: refactor upload_code_system API to use request objects
* Modernize the upload_code_system API by replacing individual parameters with structured request objects, improving type safety and API usability.
* Key changes:
* Replace multiple parameters with single `request` parameter accepting UploadRequest union type
* Add new request types: UploadRequestCsv, UploadRequestJson with format-specific validation
* Add async upload support with new async parameter and status tracking
* Extend GetCodeSystemDetailResponse with processing status enum (processing/ready/failed)
* Update documentation and examples to use new request object pattern
* Remove deprecated UploadRequestFormat enum in favor of discriminated union types
* 🌿 Generated with Fern

## 3.2.0 - 2026-02-08
* feat: add code system detail and deletion endpoints with enhanced upload
* Enhance the construe API with new code system management capabilities,
* including detailed system metadata retrieval and custom system deletion,
* plus improvements to the upload functionality with replace parameter.
* Key changes:
* Add get_code_system_detail endpoint returning full metadata including timestamps
* Add delete_custom_code_system endpoint for removing custom code systems
* Add replace parameter to upload_code_system for overwriting existing systems
* Add ForbiddenError for HTTP 403 responses from protected operations
* Clarify availability restrictions for semantic vs full-text search endpoints
* Improve parameter documentation with case-insensitive name handling
* 🌿 Generated with Fern

## 3.1.0 - 2026-02-07
* feat: add workflow support to agent API and simplify FHIR profile upload
* Added workflow integration to agent creation and simplified the FHIR profile upload process
* by deriving metadata automatically from StructureDefinition JSON.
* Key changes:
* Add workflows parameter to agent creation API for exposing workflow IDs as tools
* Simplify lang2fhir profile upload by removing version and resource parameters
* Auto-derive profile metadata from StructureDefinition JSON (id, type, url)
* Update response types to include canonical URL and resource type fields
* Enhance documentation with validation rules and usage examples
* 🌿 Generated with Fern

## 3.0.0 - 2026-02-03
* refactor: remove explicit file_type parameter from document API
* Simplify the document API by removing the required file_type parameter and implement
* automatic file type detection from content magic bytes. This change reduces API complexity
* while maintaining the same functionality through intelligent content inspection.
* Key changes:
* Remove DocumentRequestFileType enum and related imports
* Remove file_type parameter from document() method signatures
* Update documentation to clarify auto-detection behavior
* Simplify API calls by eliminating redundant MIME type specification
* 🌿 Generated with Fern

## 2.1.0 - 2026-01-29
* feat: improve API documentation and add citation support to code extraction
* This update enhances the PhenoML SDK with better API documentation and introduces citation functionality for code extraction. The changes clarify terminology server operations, add CPT usage compliance notices, and provide new source text citation capabilities.
* Key changes:
* Rename text_search_keyword_based to terminology_server_text_search for clarity
* Add Citation type for tracking source text references in extracted codes
* Include CPT usage compliance notices across relevant API endpoints
* Add include_citations configuration option for extract operations
* Improve method descriptions to clarify terminology server operations
* Add BadGatewayError handling for FHIR operations
* Add is_ancestor field to distinguish parent codes from direct extractions
* 🌿 Generated with Fern

## 2.0.0 - 2026-01-21
* feat: make provider field required in agent create/update API
* This change updates the agent creation and update endpoints to require the provider parameter instead of making it optional. The provider field now mandates FHIR provider ID(s) for agent configuration, improving API consistency and ensuring proper provider specification.
* Key changes:
* Make provider parameter required in AgentCreateRequest type definition
* Update method signatures in AgentClient, AsyncAgentClient, and RawAgentClient classes
* Reorder parameters to place required provider field before optional parameters
* Update documentation to clarify provider requirement and sandbox behavior
* Upgrade packaging dependency from version 25.0 to 26.0
* 🌿 Generated with Fern

## 1.0.0 - 2026-01-21
* refactor: remove is_active field from prompts API
* Remove the is_active field from prompt creation, update, and type definitions. Simplify the API by removing prompt activation state management and update the delete operation description to reflect actual deletion rather than soft deletion.
* Key changes:
* Remove is_active parameter from prompt create and update operations
* Update delete operation description from "soft deletes" to "deletes a prompt"
* Remove is_active field from PromptTemplate and AgentTemplate types
* Update documentation examples to remove is_active usage
* Simplify API interface by removing prompt state management
* 🌿 Generated with Fern

## 0.1.0 - 2026-01-21
* feat: add code system management and search capabilities to construe
* Expand the construe API with comprehensive code system management and search functionality, enabling users to discover available code systems, browse codes, and perform both keyword and semantic searches.
* Key changes:
* Add list_available_code_systems() to retrieve all available code systems with metadata
* Add list_codes_in_a_code_system() for paginated browsing of codes within a system
* Add get_a_specific_code() to fetch detailed information for individual codes
* Add semantic_search_embedding_based() for natural language similarity search using vector embeddings
* Add text_search_keyword_based() for fast keyword-based search with typo tolerance
* Add comprehensive error handling for NotFound, NotImplemented, and ServiceUnavailable errors
* Add new response types: CodeResponse, CodeSystemDetails, ListCodesResponse, SemanticSearchResponse, TextSearchResponse
* Update documentation with detailed usage examples and search method comparisons
* 🌿 Generated with Fern

## 1.0.0 - 2026-01-20
* refactor: remove is_active parameter from agent operations
* Remove the is_active parameter from agent create, list, and update operations
* to simplify the API interface. This breaking change removes an optional
* filtering capability from the list operation and a required field from
* create/update operations.
* Key changes:
* Remove is_active parameter from agent.create() method signature
* Remove is_active filter from agent.list() method
* Remove is_active parameter from agent.update() method signature
* Update documentation to reflect removed parameter
* Remove AgentCreateRequest.is_active field from type definitions
* 🌿 Generated with Fern

