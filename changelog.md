## 1.0.0 - 2026-01-21
* refactor: remove is_active field from agent prompts API
* This change simplifies the prompts API by removing the is_active field from both the AgentTemplate and PromptTemplate data models, along with associated client methods and documentation.
* Key changes:
* Remove is_active parameter from prompt create and update methods in sync and async clients
* Remove is_active field from AgentTemplate and PromptTemplate data models
* Update delete method description from "soft delete" to "delete" functionality
* Remove is_active documentation and examples from reference documentation
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

