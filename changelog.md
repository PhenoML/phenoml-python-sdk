## [16.7.0] - 2026-07-10
### Changed
- **Maintenance release** — no public API or behavioral changes.

## [16.6.0] - 2026-07-10
### Added
- **`client.construe.codes.phenocr(...)`** — new sync and async method (plus raw variants) that extracts medical codes from free-text clinical notes using the phenocr engine, supporting HPO, ICD-10-CM, and SNOMED_CT_US code systems.
- **`PhenocrExtractRequestSystem`** — new Pydantic model with required `name` and `version` fields for specifying the target terminology system; exported from `phenoml.construe` and `phenoml.construe.types`.
- **Expanded built-in system catalogue** — `client.construe.codes.list()` now includes UMLS 2026AA–versioned entries for CPT, HCPCS, HPO, ICD-10, ICD-10-CM, ICD-10-PCS, LOINC, RXNORM, `SNOMED_CT_US`, and `SNOMED_CT_US_LITE` alongside existing pinned-version entries.

## [16.5.0] - 2026-07-09
### Added
- **`client.implementation_guides`** — new sync and async client with `list()`, `get()`, `update()`, and `delete()` methods for managing FHIR implementation guide metadata; includes `ImplementationGuideSummary`, `ImplementationGuideDetail`, and `ImplementationGuideListResponse` models.
- **`client.profiles.profiles`** — new sync and async client (plus raw variants `RawProfilesClient` / `AsyncRawProfilesClient`) for full CRUD management of custom FHIR StructureDefinition profiles via `fhir/profiles`; exposes `ProfileSummary`, `ProfileGetResponse`, `ProfileListResponse`, `ProfileUploadRequest`, and `ProfileSummarySource`.
- **New OMOP CDM v5.4 row types and table fields** — `CareSiteRow`, `DeathRow`, `LocationRow`, `ObservationPeriodRow`, and `ProviderRow` added to `phenoml.fhir2omop`; `OmopTables` gains five matching optional table fields; linkage fields (`provider_id`, `care_site_id`, `location_id`) added to several existing row types.
- **`RequestOptions.timeout`** — new `float` field for per-request timeout in seconds; `timeout_in_seconds` is retained as a deprecated alias.

### Changed
- **`client.lang2fhir.upload_profile()`** — deprecated in favour of `client.profiles.profiles.create()`; the existing route continues to work until a future removal.
- **`PhenomlClient` / `AsyncPhenomlClient` timeout defaulting** — when a custom `httpx_client` is supplied, timeout now defaults to `None` instead of reading `httpx_client.timeout.read`.
- **`ExtractRequestSystem` built-in system list** — updated to include `HCPCS`, `ICD-10`, and `SNOMED_CT_US`; pinned version strings removed from system names.
- **`EventSource` SSE line-size guard** — raises `SSEError` if a single SSE line exceeds 1 MiB, preventing unbounded memory growth on malformed streams.
- **`CreateMultiResponseResourcesItem.source_pages`** — new optional `List[int]` field containing 1-indexed source document page numbers for resources extracted by the `/lang2fhir/document/multi` endpoint.

## [16.4.0] - 2026-06-23
### Added
- **`client.voice.voice.transcribe(...)`** — new sync and async method that accepts raw audio bytes (WAV, FLAC, MP3, OGG/WebM Opus) and returns a `TranscribeResponse` with the full transcript, supporting up to ~5 minutes of audio per request.
- **`RawVoiceClient`** and **`AsyncRawVoiceClient`** — new clients under `phenoml.voice.voice` exposing `transcribe(...)` with support for `bytes`, `Iterator[bytes]`, or `AsyncIterator[bytes]` input and an optional BCP-47 `language` hint.
- **`phenoml.voice.TranscribeResponse`** — new response type with a `transcript` field returned by the transcription endpoint.
- **`phenoml.voice.errors`** — new typed error classes (`BadRequestError`, `UnauthorizedError`, `PaymentRequiredError`, `ContentTooLargeError`, `BadGatewayError`, `ServiceUnavailableError`, `GatewayTimeoutError`) raised by the voice service.

## [16.3.0] - 2026-06-18
### Added
- **`phenoml.agent.errors.ConflictError`** — new `ApiError` subclass raised by `client.agent.chat.send(...)` and `client.agent.chat.stream(...)` for HTTP 409 responses when a session already has an active turn.

### Changed
- **`client.agent.chat.send(...)` and `client.agent.chat.stream(...)` `session_id` parameter** — docstring now states that only one request may be active per session at a time and overlapping turns return `409 Conflict`.
- **`client.fhir2omop.create(...)`** — docstring now lists the supported FHIR resource-to-OMOP table mappings and clarifies that unsupported resource types are accepted but ignored.
- **`CreateOmopResponse.dropped`** — field description now clarifies that only supported resources missing required subject/patient, code, or medication reference data appear in `dropped`; unsupported resource types are ignored.

## [16.2.0] - 2026-06-15
### Added
- **`Provider`** — `"aidbox"` is now a supported FHIR provider value in the `Provider` union type.

## [16.1.0] - 2026-06-15
### Added
- **`ConditionOccurrenceRow.visit_occurrence_id`**, **`DrugExposureRow.visit_occurrence_id`**, **`MeasurementRow.visit_occurrence_id`**, **`ObservationRow.visit_occurrence_id`**, and **`ProcedureOccurrenceRow.visit_occurrence_id`** — new optional field linking each clinical OMOP row back to its `visit_occurrence` row.
- **`MeasurementRow.operator_concept_id`** — new optional field carrying the OMOP "Meas Value Operator" standard concept (`<`, `<=`, `>`, `>=`) parsed from a FHIR `valueQuantity.comparator` or numeric-string value; `0` when no operator is present.

### Changed
- **`MappingEntry.target_code`** — field semantics updated: now populated for `ALREADY_STANDARD` and `MAPPED` rows (the standard concept's own code) in addition to `UNCHECKED` suggestions; omitted only for `UNMAPPED` rows.
- **`client.fhir2omop.create()` docstring** — clarifies that `concept_id=0` covers both `UNMAPPED` (no standard match) and `UNCHECKED` (unverified text-only suggestion), and documents that `operator_concept_id` is the one non-zero non-resolved concept on measurement rows.

## [16.0.0] - 2026-06-15
### Breaking Changes
- **`phenoml.fhir2omop.MappingReportEntry`** — renamed to **`MappingEntry`**; update all imports and type annotations to use `MappingEntry`.
- **`phenoml.fhir2omop.ScanSummary`** — renamed to **`Summary`**; update all imports and type annotations to use `Summary`.
- **`phenoml.fhir2omop.CreateOmopResponse`** — fields `report`, `scan_summary`, and `mode` removed; replace `report` with `mappings` (`List[MappingEntry]`), `scan_summary` with `summary` (`Summary`), and remove any references to `mode`.

### Added
- **`phenoml.fhir2omop.MappingEntry`** — new Pydantic model describing how a single source coding resolved to an OMOP standard concept, exposing fields such as `omop_id`, `source_code`, `target_vocabulary`, `mapping_status`, and `note`.
- **`phenoml.fhir2omop.Summary`** — new Pydantic model carrying data-quality headline metrics: `codes_already_standard`, `codes_normalized`, `codes_unmapped`, and `off_vocab_rate`.
- **`phenoml.fhir2omop.CreateOmopResponse.dropped`** — new top-level field listing resources that could not be shaped into an OMOP row (previously nested under `scan_summary.dropped_resources`).
- **`phenoml.fhir2omop.CreateOmopResponse.vocab_version`** — new top-level field reporting the OMOP vocabulary release codes were resolved against (e.g. `"v20240229"`).
- **`phenoml.fhir2omop.ServiceUnavailableError`** — new `ApiError` subclass raised when the API returns HTTP 503; callers may now catch this explicitly.

### Changed
- **`client.fhir2omop.create()` OpenAPI spec** — endpoint description updated to document both `resolved` and `structural` modes in detail, including a `resolved_mapping` response example.

## 15.2.0 - 2026-06-09
### Added
* **`phenoml.fhir2omop.ScanSummary`** — five resolver-telemetry fields added (`resolved_vocab_version`, `concept_resolver_note`, `concepts_bridged`, `concept_candidates_truncated`, `construe_resolutions`) reporting the OMOP vocabulary release used and where concept resolution was degraded, bridged, truncated, or fell back to (and billed) the construe tier.
### Changed
* **`client.fhir2omop.create()`** — now defaults to `mode="resolved"`, filling clinical `concept_id`s via the concept-resolver service; the former structural-only behavior (all clinical `concept_id`s `0`) now occurs only when no resolver is configured and is reported as `mode="structural"`.
* **`phenoml.fhir2omop.MappingReportEntry.mapping_status`** — adds the `MAPPED` value, returned in resolved mode when a coding is mapped to a standard concept via the OMOP "Maps to" crosswalk or UMLS-CUI bridge.
* **`phenoml.fhir2omop.MappingReportEntry.equivalence`** — field removed; per-coding mapping confidence is now conveyed by `mapping_status`. (Finalizes the fhir2omop response shape first shipped earlier today in 15.1.0.)
* **`phenoml.fhir2omop.MappingReportEntry.target_code`** — now omitted for codings resolved directly by the concept-resolver (which returns the concept id/name/vocabulary but not its `concept_code`); still populated for structural / construe-tier matches.

## 15.1.0 - 2026-06-09
### Added
* **`client.fhir2omop.create()`** — new method posting FHIR R4 resources or a Bundle to `POST /fhir2omop/create` and returning OMOP CDM v5.4 rows; structural mode only, so all clinical `concept_id`s are `0` (the vocabulary crosswalk is a later release).
* **`phenoml.fhir2omop.CreateOmopRequest` / `CreateOmopResponse`** — request carries `fhir_resources` (single resource or Bundle); response exposes `tables`, `report`, and `scan_summary`.
* **`phenoml.fhir2omop.OmopTables`** and the row types `PersonRow`, `ConditionOccurrenceRow`, `DrugExposureRow`, `MeasurementRow`, `ObservationRow`, `ProcedureOccurrenceRow`, `VisitOccurrenceRow` — typed OMOP CDM table output.
* **`phenoml.fhir2omop.MappingReportEntry` / `DroppedResource` / `ScanSummary`** — Usagi-shaped per-coding mapping report and White Rabbit-style scan summary.

## 15.0.3 - 2026-06-06
### Changed
* **Maintenance release** — no API or behavioral changes; regenerated tooling/metadata and re-synced the bundled `openapi.json` (same API surface as 15.0.2).

## 15.0.2 - 2026-06-06
### Changed
* **Packaging — bundled `openapi.json`** — restored to the sdist/wheel (it was temporarily omitted in 15.0.1); installed packages again include `phenoml/openapi/openapi.json`.

## 15.0.1 - 2026-06-06
### Changed
* **`phenoml.core.serialization` / `phenoml.core.pydantic_utilities`** — internal performance refactor: resolved type hints, pydantic `TypeAdapter` instances, and alias-conversion decisions are now cached, and the recursive alias walk is skipped when a type carries no field aliases (the hot path for SSE streaming). `parse_sse_obj` was simplified to always JSON-parse the SSE `data` field; the removed event-level discrimination path was unused by this SDK (the sole SSE stream, agent chat, is data-level discriminated), so streaming behavior is unchanged.
* **`aiohttp` extra** — the optional `aiohttp` dependency floor is raised to `>=3.14.0` (was `>=3.13.4`); installing `phenoml[aiohttp]` now requires aiohttp 3.14+.
* **Packaging — bundled `openapi.json`** — temporarily not shipped in the sdist/wheel for this release; restored in 15.0.2. (One-time step so Fern replay preserves the packaging automatically on future regens.)

## 15.0.0 - 2026-06-02
### Breaking Changes
* **`client.agent.chat(...)` / `client.agent.stream_chat(...)` / `client.agent.get_chat_messages(...)`** — removed from `AgentClient`/`AsyncAgentClient`; the three chat methods now live on a new `client.agent.chat` sub-client. Rewrite call sites as `client.agent.chat.send(...)` / `client.agent.chat.stream(...)` / `client.agent.chat.list_messages(...)`.
* **`phenoml.agent.GetChatMessagesResponse` / `GetChatMessagesRequestRole` / `GetChatMessagesRequestOrder`** — removed; replaced by `phenoml.agent.chat.ListMessagesResponse` / `ListMessagesRequestRole` / `ListMessagesRequestOrder` (also re-exported from `phenoml.agent`). Update imports.
* **`client.construe.upload_code_system(...)` / `list_code_systems()` / `get_code_system(...)` / `delete_code_system(...)` / `export_code_system(...)`** — removed from `ConstrueClient`/`AsyncConstrueClient`; the code-system methods now live on a new `client.construe.code_systems` sub-client. Rewrite as `client.construe.code_systems.upload(...)` / `.list()` / `.find(...)` / `.delete(...)` / `.export(...)` (note `get_code_system` → `find`).
* **`client.construe.extract_codes(...)` / `list_codes(...)` / `get_code(...)` / `search_semantic(...)` / `search_text(...)`** — removed from `ConstrueClient`/`AsyncConstrueClient`; the code methods now live on a new `client.construe.codes` sub-client. Rewrite as `client.construe.codes.extract(...)` / `.list(...)` / `.lookup(...)` / `.search_semantic(...)` / `.search_text(...)` (note `get_code` → `lookup`); `submit_feedback(...)` stays on `client.construe`.
* **`phenoml.construe.UploadCodeSystemResponse`** — renamed and moved to `phenoml.construe.code_systems.UploadResponse` (also re-exported from `phenoml.construe` as `UploadResponse`); update imports and annotations on the upload method.
* **`client.fhir_provider.add_auth_config(...)` / `set_active_auth_config(...)` / `remove_auth_config(...)`** — removed from `FhirProviderClient`/`AsyncFhirProviderClient`; the auth-config methods now live on a new `client.fhir_provider.auth_config` sub-client. Rewrite as `client.fhir_provider.auth_config.add(...)` / `.set_active(...)` / `.remove(...)`.
* **`phenoml.fhir_provider.RemoveAuthConfigResponse`** — renamed and moved to `phenoml.fhir_provider.auth_config.RemoveResponse` (also re-exported from `phenoml.fhir_provider` as `RemoveResponse`); update imports.
* **`client.fhir.create(...)` / `upsert(...)`** — the typed body parameters (`resource_type`, `id`, `meta`) are removed in favor of a single `request: typing.Any`, and the return type changes from `FhirResource` to `typing.Any`; pass the full FHIR resource as one dict and treat the result as untyped JSON.
* **`client.fhir.execute_bundle(...)`** — the typed body parameters (`entry`, `total`) are removed in favor of a single `request: typing.Any`, and the return type changes from `FhirBundle` to `typing.Any`; pass the full bundle as one dict and treat the result as untyped JSON.
* **`client.fhir.search(...)`** — the `query_parameters` parameter is removed and the return type changes from `SearchResponse` to `typing.Any`; build the query into `fhir_path` and treat the result as untyped JSON.
* **`client.fhir.patch(...)` / `delete(...)`** — return types change to `typing.Any` (from `FhirResource` / `typing.Dict[str, typing.Any]`); `patch`'s `request: typing.Sequence[PatchRequestBodyItem]` parameter is unchanged.
* **`phenoml.fhir.FhirResource` / `FhirResourceMeta` / `FhirBundle` / `FhirBundleEntryItem` / `FhirBundleEntryItemRequest` / `FhirBundleEntryItemRequestMethod` / `FhirBundleEntryItemResponse` / `SearchResponse` / `ErrorResponse`** — removed from `phenoml.fhir` and `phenoml.fhir.types`; remove any imports or annotations referencing them (FHIR proxy payloads are now opaque). `PatchRequestBodyItem` / `PatchRequestBodyItemOp` are retained.
* **`phenoml.fhir.BadGatewayError` / `BadRequestError` / `InternalServerError` / `NotFoundError` / `ServiceUnavailableError` / `TooManyRequestsError` / `UnauthorizedError`** — the entire `phenoml.fhir.errors` subpackage was removed; remove any imports and `except` clauses for these classes and catch `phenoml.core.ApiError` instead.
* **`phenoml.summary.templates.TemplatesListResponse` / `TemplatesGetResponse` / `TemplatesUpdateResponse` / `TemplatesDeleteResponse`** — renamed to `phenoml.summary.templates.ListResponse` / `GetResponse` / `UpdateResponse` / `DeleteResponse` (dropping the `Templates` prefix added in 14.0.0; also re-exported from `phenoml.summary`); update imports and annotations on the `client.summary.templates` methods.
* **`client.tools.mcp_server`** — the `mcp_server` sub-client (and its nested `.tools`) is removed; server CRUD moves to `client.tools.mcp_servers` (`create` / `list` / `get` / `delete`) and tool CRUD moves to a sibling `client.tools.mcp_tools` (`list` / `get` / `delete`). Rewrite `client.tools.mcp_server.<m>(...)` → `client.tools.mcp_servers.<m>(...)` and `client.tools.mcp_server.tools.<m>(...)` → `client.tools.mcp_tools.<m>(...)`.
* **`phenoml.tools.FailedDependencyError`** — removed (HTTP 424 is no longer raised); remove any imports or `except` clauses referencing it.
* **`phenoml.lang2fhir.FailedDependencyError`** — removed (HTTP 424 is no longer raised); remove any imports or `except` clauses referencing it.
### Added
* **`client.agent.chat`** — new sub-client (`ChatClient` / `AsyncChatClient`) exposing `send(...)`, `stream(...)`, and `list_messages(...)` for agent chat.
* **`phenoml.agent.GatewayTimeoutError`** — new error class (HTTP 504) in `phenoml.agent.errors` raised when an upstream agent operation times out.
* **`client.construe.code_systems`** — new sub-client (`CodeSystemsClient` / `AsyncCodeSystemsClient`) exposing `upload(...)`, `list()`, `find(...)`, `delete(...)`, `export(...)`.
* **`client.construe.codes`** — new sub-client (`CodesClient` / `AsyncCodesClient`) exposing `extract(...)`, `list(...)`, `lookup(...)`, `search_semantic(...)`, `search_text(...)`.
* **`client.fhir_provider.auth_config`** — new sub-client (`AuthConfigClient` / `AsyncAuthConfigClient`) exposing `add(...)`, `set_active(...)`, `remove(...)`.
* **`client.tools.mcp_servers`** and **`client.tools.mcp_tools`** — new sub-clients replacing the former `mcp_server` sub-client and its nested `tools`.
* **`phenoml.tools.NotFoundError`** — new error class (HTTP 404) in `phenoml.tools.errors`.
* **`phenoml.lang2fhir.NotFoundError` / `ClientClosedRequestError` / `GatewayTimeoutError`** — new error classes (HTTP 404 / 499 / 504) in `phenoml.lang2fhir.errors`, raised by the lang2fhir endpoints.
### Changed
* **`client.workflows.get(...)` / `update(...)` / `delete(...)`** — now raise the existing `phenoml.workflows.GatewayTimeoutError` on HTTP 504 (previously only `execute(...)` did); no API surface change.

## 14.0.0 - 2026-05-25
### Breaking Changes
* **`client.summary.list_templates()` / `create_template()` / `get_template()` / `update_template()` / `delete_template()`** — removed from `SummaryClient`/`AsyncSummaryClient`; the five template CRUD methods now live on a new `client.summary.templates` sub-client. Rewrite call sites as `client.summary.templates.list()` / `create()` / `get(...)` / `update(...)` / `delete(...)`. HTTP routes are unchanged.
* **`phenoml.summary.SummaryListTemplatesResponse` / `SummaryGetTemplateResponse` / `SummaryUpdateTemplateResponse` / `SummaryDeleteTemplateResponse`** — removed; replaced by `phenoml.summary.templates.TemplatesListResponse` / `TemplatesGetResponse` / `TemplatesUpdateResponse` / `TemplatesDeleteResponse` (also re-exported from `phenoml.summary`). Update imports.
* **`client.authtoken.auth.get_token()`** — the entire `authtoken.auth` subpackage was removed; call `client.authtoken.get_token(...)` directly (sync and async). Replace any imports of `phenoml.authtoken.auth.AuthClient` / `AsyncAuthClient` with `phenoml.authtoken.AuthtokenClient` / `AsyncAuthtokenClient`.
* **`client.construe.list_available_code_systems()` → `list_code_systems()`** — method renamed (sync, async, and raw variants).
* **`client.construe.get_code_system_detail()` → `get_code_system()`** — method renamed.
* **`client.construe.delete_custom_code_system()` → `delete_code_system()`** — method renamed.
* **`client.construe.export_custom_code_system()` → `export_code_system()`** — method renamed.
* **`client.construe.list_codes_in_a_code_system()` → `list_codes()`** — method renamed.
* **`client.construe.get_a_specific_code()` → `get_code()`** — method renamed.
* **`client.construe.semantic_search_embedding_based()` → `search_semantic()`** — method renamed.
* **`client.construe.terminology_server_text_search()` → `search_text()`** — method renamed.
* **`client.construe.submit_feedback_on_extraction_results()` → `submit_feedback()`** — method renamed.
* **`client.lang2fhir.extract_multiple_fhir_resources_from_a_document()` → `client.lang2fhir.document_multi()`** — method renamed (sync, async, and raw variants).
* **`phenoml.construe.ConstrueUploadCodeSystemResponse`** — renamed to `phenoml.construe.UploadCodeSystemResponse`.
* **`phenoml.fhir.FhirSearchResponse`** — renamed to `phenoml.fhir.SearchResponse`.
* **`phenoml.fhir.FhirPatchRequestBodyItem` / `FhirPatchRequestBodyItemOp`** — renamed to `phenoml.fhir.PatchRequestBodyItem` / `PatchRequestBodyItemOp`.
* **`phenoml.fhir_provider.FhirProviderDeleteResponse` / `FhirProviderRemoveAuthConfigResponse`** — renamed to `phenoml.fhir_provider.DeleteResponse` / `RemoveAuthConfigResponse`.
* **`phenoml.lang2fhir.Lang2FhirUploadProfileResponse`** — renamed to `phenoml.lang2fhir.UploadProfileResponse`.
* **`phenoml.agent.Agent*` request and response types** — `Agent` prefix dropped: `AgentListResponse` → `ListResponse`, `AgentDeleteResponse` → `DeleteResponse`, `AgentGetChatMessagesResponse` → `GetChatMessagesResponse`, `AgentGetChatMessagesRequestRole` → `GetChatMessagesRequestRole`, `AgentGetChatMessagesRequestOrder` → `GetChatMessagesRequestOrder` (still under `phenoml.agent`).
* **`phenoml.workflows.WorkflowsGetResponse` / `WorkflowsUpdateResponse` / `WorkflowsDeleteResponse`** — renamed to `phenoml.workflows.GetResponse` / `UpdateResponse` / `DeleteResponse`.
### Added
* **`client.summary.templates`** — new sub-client (`TemplatesClient` / `AsyncTemplatesClient`) exposing `list()`, `create()`, `get()`, `update()`, `delete()` for summary templates.
* **`phenoml.summary.templates`** — new submodule exporting `TemplatesListResponse`, `TemplatesGetResponse`, `TemplatesUpdateResponse`, `TemplatesDeleteResponse` (also re-exported from `phenoml.summary`).
* **`phenoml.workflows.GatewayTimeoutError`** — new error class (HTTP 504) raised by `client.workflows.execute()` / async equivalent (and corresponding raw clients) when the upstream workflow execution times out.

## 13.0.0 - 2026-05-15
### Breaking Changes
* **`call()`** (`ToolsClient`, `AsyncToolsClient`, `RawToolsClient`, `AsyncRawToolsClient`) — the method for calling an MCP server tool has been removed; delete any call sites using `client.tools.mcp_server.tools.call(...)`.
* **`McpServerToolCallResponse`** — type removed from `phenoml.tools` and `phenoml.tools.types`; remove any imports or type annotations that reference it.

## 12.0.0 - 2026-05-13
### Breaking Changes
* **`load_defaults`** — method removed from `PromptsClient`, `AsyncPromptsClient`, `RawPromptsClient`, and `AsyncRawPromptsClient`; delete any call sites using `agent.prompts.load_defaults()`.
* **`FhirBundle`**, **`FhirBundleEntryItem`**, **`FhirResource`**, and **`CreateSummaryRequestFhirResources`** — types removed from `phenoml.summary`; update any imports or type annotations that reference them.
* **`McpServerResponseData`** renamed to **`McpServer`** and **`McpServerToolResponseData`** renamed to **`McpServerTool`** in `phenoml.tools`; replace all imports and type annotations with the new names.
### Added
* **`McpServer`** — new public model representing an MCP server record, exported from `phenoml.tools`.
* **`McpServerResponse.mcp_servers`** — new optional `List[McpServer]` field returned by the MCP server create and list endpoints.
* **`McpServerResponse.mcp_server_tools`** and **`McpServerToolResponse.mcp_server_tools`** — new optional list fields carrying tools discovered at MCP server create time or via the list endpoint.

## 11.0.0 - 2026-05-11
### Breaking Changes
* **`search_fhir_resources`** (`ToolsClient`, `AsyncToolsClient`, `RawToolsClient`, `AsyncRawToolsClient`) — the `practitioner_id` parameter has been removed; remove any `practitioner_id=...` argument from call sites.
* **`document_multi`** / **`extract_multiple_fhir_resources_from_a_document`** (`RawLang2FhirClient`, `AsyncRawLang2FhirClient`, `Lang2FhirClient`, `AsyncLang2FhirClient`) — now returns `DocumentMultiResponse` instead of `CreateMultiResponse`; update type annotations and any field access that is unique to `CreateMultiResponse`.
### Added
* **`DocumentConfig`** — new optional `config` parameter on `document` and `document_multi` / `extract_multiple_fhir_resources_from_a_document` (sync and async) for per-request document processing configuration.
* **`DocumentMultiResponse`** — new dedicated response model extending `CreateMultiResponse` with an optional `page_classifications` list populated when a `PageFilter` is supplied.
* **`PageFilter`** and **`PageClassification`** — new models enabling per-page LLM-based pre-extraction filtering; irrelevant pages are dropped before FHIR extraction and each page's decision is captured in `PageClassification`.
* **`max_retries`** — new optional parameter on `PhenomlClient` and `AsyncPhenomlClient` (default `2`) for setting the client-wide retry count; per-request `RequestOptions.max_retries` still takes precedence.
* **`DefaultAioHttpClient`**, **`DefaultAsyncHttpxClient`**, and the **`phenoml[aiohttp]`** extra — new convenience async HTTP client classes and optional install extra for aiohttp-backed async transport.
### Changed
* **`CreateMultiResponseResourcesItem.original_text`** — new optional field holding the verbatim source text excerpt; the existing `description` field now holds the context-enriched rewritten excerpt.
### Fixed
* **SSE streaming** (`iter_sse` / `aiter_sse`) — incremental charset decoding and `\r\n` / bare `\r` line-ending normalization now prevent dropped or malformed events on non-Unix line endings.
* **Path parameter encoding** in prompts endpoints now uses `encode_path_param` instead of `jsonable_encoder`, ensuring correct URL-safe encoding for prompt IDs.

## 10.5.0 - 2026-05-01
### Added
* **`CreateMultiRequestValidationMethod`** and **`DocumentMultiRequestValidationMethod`** — new enums with values `"none"`, `"check"`, and `"fix"` controlling FHIR structure validation applied to the generated bundle.
* **`validation_method`** — new optional parameter on `create_multi` and `extract_multiple_fhir_resources_from_a_document` (both `Lang2FhirClient` and `AsyncLang2FhirClient`); `"check"` validates the bundle and returns results, `"fix"` additionally attempts LLM-based auto-correction (up to 3 passes).
* **`CreateMultiResponse.validation`** — new optional field of type `CreateMultiResponseValidation` populated when `validation_method` is `"check"` or `"fix"`; contains per-pass issues, statistics, fix status, attempt count, and a human-readable summary.
* **`CreateMultiResponseValidation`**, **`CreateMultiResponseValidationPassesItem`**, **`CreateMultiResponseValidationPassesItemIssuesItem`**, **`CreateMultiResponseValidationPassesItemIssuesItemSeverity`**, and **`CreateMultiResponseValidationPassesItemStats`** — new response models representing the full FHIR validation result structure.

## 10.4.0 - 2026-04-29
### Added
* **`CodeCategory`** — new model (fields: `uri`, `label`) representing a higher-level grouping for an extracted code (e.g. an HPO category term); exported from `phenoml.construe`.
* **`ExtractRequestConfigChunkingMethod`** gains a new `"fasthpocr"` value — extracts HPO concepts directly with category annotations and citation support; requires `system: HPO` and causes most other config options to be ignored.
* **`ExtractedCodeResult.categories`** — new optional `List[CodeCategory]` field populated when using full-extraction chunking methods such as `"fasthpocr"`.
### Changed
* **`ExtractRequestConfig.include_rationale`** — citations are now also supported when `chunking_method` is `"fasthpocr"` (previously documented as `"sentences"` and `"clinical_ner_extract"` only).

## 10.3.0 - 2026-04-24
### Added
* **`ExtractRequestConfigChunkingMethod`** gains a new `"clinical_ner_extract"` value — extracts clinical concepts (problems, tests, treatments) and uses each concept as a chunk; supports source text citations.
* **`ExtractRequestConfigValidationMethod`** gains a new `"chunk_code_jaccard_similarity"` value — validates codes using token-level Jaccard similarity between the source text chunk and the code description.
* **`ExtractRequestConfig.chunk_code_jaccard_similarity_filtering_threshold`** — new optional `float` field (0.0–1.0) controlling the minimum Jaccard similarity score required when using the `"chunk_code_jaccard_similarity"` validation method.
### Changed
* **`ExtractRequestConfig.include_rationale`** — citations (character-offset text spans) are now supported when `chunking_method` is `"sentences"` or `"clinical_ner_extract"` (previously documented as `"sentences"` only).

## 10.2.0 - 2026-04-14
* The `create_multi`, `extract_multiple_fhir_resources_from_a_document`, and `upload_profile` methods on `Lang2FhirClient` and `AsyncLang2FhirClient` now accept an optional `implementation_guide` parameter. When specified, profiles from the named Implementation Guide are included alongside US Core profiles during resource detection (US Core is always the base layer; custom IG profiles are additive). The `upload_profile` method also accepts a new optional `profile_context` parameter — a natural-language hint injected into the LLM prompt to guide profile selection within the IG (max 2000 characters; last write wins per IG).

## 10.1.0 - 2026-04-13
* The `create_multi` and `extract_multiple_fhir_resources_from_a_document` methods on `Lang2FhirClient` and `AsyncLang2FhirClient` now accept an optional `detection_effort` parameter. Set it to `"standard"` (default behavior, runs detection once) or `"deep"` (runs detection multiple times for higher recall at the cost of additional latency). The new `CreateMultiRequestDetectionEffort` and `DocumentMultiRequestDetectionEffort` types are available from `phenoml.lang2fhir`.

## 10.0.1 - 2026-04-13
* docs: expand consistency_effort field documentation
* Update the `consistency_effort` field docstring in `ExtractRequestConfig`
* to clarify how consistency is applied depending on the active configuration.
* The previous description was vague; the updated version explains exactly
* when consistency is applied to the validation step versus the relevance
* ranking step.
* Key changes:
* Clarify "borderline codes" → "borderline results" for accuracy
* Document that when `validation_method` is set (non-"none"), consistency
* applies to the validation step (unanimous validation across rounds)
* Document that when `validation_method` is "none" and
* `min_context_relevance > 0`, consistency applies to the relevance
* ranking step (chunks must pass threshold in every round)
* 🌿 Generated with Fern

## 10.0.0 - 2026-04-03
* The `generate_token` method has been removed from `AuthClient` and `AsyncAuthClient`. Replace calls to `client.authtoken.auth.generate_token(username=..., password=...)` with `client.authtoken.auth.get_token(...)`. The `AuthGenerateTokenResponse`, `BadRequestErrorBody`, and `UnauthorizedErrorBody` types have also been removed from the public API. Additionally, the minimum supported Python version is now 3.10.
* The SDK now surfaces a dedicated `ParsingError` exception (available via `from phenoml.core import ParsingError`) when a server response is valid JSON but fails to deserialize into the expected model. Previously, a raw Pydantic `ValidationError` would propagate unhandled in these cases. This makes it easier to distinguish malformed API responses from other HTTP errors.
* The SDK now raises a `ParsingError` exception (available from `phenoml.core.parse_error`) when a server response cannot be parsed against the expected schema. This replaces unhandled Pydantic `ValidationError` exceptions with a structured error that includes the HTTP status code, response headers, response body, and the underlying validation cause — making it easier to diagnose unexpected API responses.
* The SDK now raises a `ParsingError` (instead of a bare Pydantic `ValidationError`) when a server response cannot be deserialized. The `ParsingError` includes the HTTP status code, response headers, and response body alongside the original validation error, making it easier to diagnose unexpected API responses.

## 9.4.0 - 2026-03-31
* The extraction API now supports configurable consistency levels through the new `consistency_effort` parameter on `ExtractRequestConfig`. Set this to "low", "medium", or "high" to apply stricter filtering that removes borderline codes which may vary between repeated requests, improving determinism at the cost of additional latency.

## 9.3.0 - 2026-03-26
* The extraction API now supports context-based relevance filtering. Use the new `extraction_context` parameter to describe your extraction goal and `min_context_relevance` to set a threshold that automatically filters out irrelevant document chunks before extraction, reducing noise and processing costs.

## 9.2.0 - 2026-03-17
* The SDK now supports "meditech" as a FHIR provider option, enabling integration with Meditech healthcare systems.

## 9.1.0 - 2026-03-11
* The workflow execution methods now support an optional `preview` parameter. When set to true, workflows return mock resources instead of persisting data to the FHIR server, enabling safe testing and development.

## 9.0.0 - 2026-03-11
* The `ErrorResponse` type has been removed from the summary module. If your code references `phenoml.summary.ErrorResponse` or imports it directly, you'll need to update your error handling logic to use the appropriate error types for your specific use case.

## 8.1.0 - 2026-03-09
* feat: add ServiceUnavailableError and TooManyRequestsError handling
* Add comprehensive error handling for HTTP 429 (Too Many Requests) and HTTP 503 (Service Unavailable) status codes across all FHIR client methods. This improves the client's robustness by properly handling rate limiting and temporary service unavailability scenarios.
* Key changes:
* Add ServiceUnavailableError class for HTTP 503 responses
* Add TooManyRequestsError class for HTTP 429 responses with structured ErrorResponse body
* Update all sync and async client methods to handle these new error types
* Add proper imports and exports in module initialization files
* 🌿 Generated with Fern

## 8.0.0 - 2026-03-04

### Breaking Changes

- **Authentication**: Replaced username/password authentication with OAuth 2.0 client credentials. The client now accepts `client_id` and `client_secret` parameters (defaulting to `PHENOML_CLIENT_ID` and `PHENOML_CLIENT_SECRET` environment variables). Tokens are automatically obtained and refreshed via the `/v2/auth/token` endpoint. A `token` callable is also supported for pre-existing tokens.
- **Client renamed**: The main client class is now `PhenomlClient` (was `PhenoMLClient` wrapper / `phenoml` base class).
- **Wrapper client removed**: The custom `wrapper_client.py` has been removed. Use `PhenomlClient` directly.

### Migration Guide

**Authentication** — replace username/password with client credentials:

```python
# Before
from phenoml import PhenoMLClient
client = PhenoMLClient(
    username="user",
    password="pass",
    base_url="https://yourinstance.app.pheno.ml",
)

# After (option 1: env vars PHENOML_CLIENT_ID and PHENOML_CLIENT_SECRET)
from phenoml import PhenomlClient
client = PhenomlClient(base_url="https://yourinstance.app.pheno.ml")

# After (option 2: explicit credentials)
from phenoml import PhenomlClient
client = PhenomlClient(
    client_id="YOUR_CLIENT_ID",
    client_secret="YOUR_CLIENT_SECRET",
    base_url="https://yourinstance.app.pheno.ml",
)

# After (option 3: pre-existing token)
from phenoml import PhenomlClient
client = PhenomlClient(
    token=lambda: "YOUR_TOKEN",
    base_url="https://yourinstance.app.pheno.ml",
)
```

**Import updates:**

```python
# Before
from phenoml import PhenoMLClient

# After
from phenoml import PhenomlClient
```

### Added

- New `/v2/auth/token` OAuth 2.0 client credentials endpoint with `TokenResponse`, `OAuthError`, and `OAuthErrorError` types.
- `OAuthTokenProvider` and `AsyncOAuthTokenProvider` for automatic token acquisition and refresh.
- Structured logging support via new `logging` module.
- `datetime_utils` module for date/time handling.
- Python 3.13, 3.14, and 3.15 support.

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
