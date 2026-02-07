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

