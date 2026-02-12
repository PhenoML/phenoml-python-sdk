## 5.0.0 - 2026-02-12
* refactor: simplify code upload system API and remove user_id fields
* Refactored the code upload system to use individual parameters instead of a complex request object, improving API usability and maintainability. The upload process now returns immediately and processes asynchronously, with status polling available via GET endpoint.
* Key changes:
* Replace UploadRequest union type with individual parameters in upload_code_system method
* Change from synchronous to asynchronous processing model with 202 Accepted response
* Remove user_id fields from multiple template classes for simplified data models
* Add name and version fields to upload response for better tracking
* Update documentation to reflect asynchronous processing workflow
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

