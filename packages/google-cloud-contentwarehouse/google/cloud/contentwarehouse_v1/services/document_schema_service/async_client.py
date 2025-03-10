# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import (
    Dict,
    Mapping,
    MutableMapping,
    MutableSequence,
    Optional,
    Sequence,
    Tuple,
    Type,
    Union,
)

from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core.client_options import ClientOptions
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

from google.cloud.contentwarehouse_v1 import gapic_version as package_version

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.longrunning import operations_pb2
from google.protobuf import timestamp_pb2  # type: ignore

from google.cloud.contentwarehouse_v1.services.document_schema_service import pagers
from google.cloud.contentwarehouse_v1.types import (
    document_schema as gcc_document_schema,
)
from google.cloud.contentwarehouse_v1.types import document_schema
from google.cloud.contentwarehouse_v1.types import document_schema_service

from .client import DocumentSchemaServiceClient
from .transports.base import DEFAULT_CLIENT_INFO, DocumentSchemaServiceTransport
from .transports.grpc_asyncio import DocumentSchemaServiceGrpcAsyncIOTransport


class DocumentSchemaServiceAsyncClient:
    """This service lets you manage document schema."""

    _client: DocumentSchemaServiceClient

    DEFAULT_ENDPOINT = DocumentSchemaServiceClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = DocumentSchemaServiceClient.DEFAULT_MTLS_ENDPOINT

    document_schema_path = staticmethod(
        DocumentSchemaServiceClient.document_schema_path
    )
    parse_document_schema_path = staticmethod(
        DocumentSchemaServiceClient.parse_document_schema_path
    )
    location_path = staticmethod(DocumentSchemaServiceClient.location_path)
    parse_location_path = staticmethod(DocumentSchemaServiceClient.parse_location_path)
    common_billing_account_path = staticmethod(
        DocumentSchemaServiceClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        DocumentSchemaServiceClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(DocumentSchemaServiceClient.common_folder_path)
    parse_common_folder_path = staticmethod(
        DocumentSchemaServiceClient.parse_common_folder_path
    )
    common_organization_path = staticmethod(
        DocumentSchemaServiceClient.common_organization_path
    )
    parse_common_organization_path = staticmethod(
        DocumentSchemaServiceClient.parse_common_organization_path
    )
    common_project_path = staticmethod(DocumentSchemaServiceClient.common_project_path)
    parse_common_project_path = staticmethod(
        DocumentSchemaServiceClient.parse_common_project_path
    )
    common_location_path = staticmethod(
        DocumentSchemaServiceClient.common_location_path
    )
    parse_common_location_path = staticmethod(
        DocumentSchemaServiceClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentSchemaServiceAsyncClient: The constructed client.
        """
        return DocumentSchemaServiceClient.from_service_account_info.__func__(DocumentSchemaServiceAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            DocumentSchemaServiceAsyncClient: The constructed client.
        """
        return DocumentSchemaServiceClient.from_service_account_file.__func__(DocumentSchemaServiceAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return DocumentSchemaServiceClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> DocumentSchemaServiceTransport:
        """Returns the transport used by the client instance.

        Returns:
            DocumentSchemaServiceTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(DocumentSchemaServiceClient).get_transport_class,
        type(DocumentSchemaServiceClient),
    )

    def __init__(
        self,
        *,
        credentials: Optional[ga_credentials.Credentials] = None,
        transport: Union[str, DocumentSchemaServiceTransport] = "grpc_asyncio",
        client_options: Optional[ClientOptions] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the document schema service client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.DocumentSchemaServiceTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = DocumentSchemaServiceClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def create_document_schema(
        self,
        request: Optional[
            Union[document_schema_service.CreateDocumentSchemaRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        document_schema: Optional[gcc_document_schema.DocumentSchema] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcc_document_schema.DocumentSchema:
        r"""Creates a document schema.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_create_document_schema():
                # Create a client
                client = contentwarehouse_v1.DocumentSchemaServiceAsyncClient()

                # Initialize request argument(s)
                document_schema = contentwarehouse_v1.DocumentSchema()
                document_schema.display_name = "display_name_value"

                request = contentwarehouse_v1.CreateDocumentSchemaRequest(
                    parent="parent_value",
                    document_schema=document_schema,
                )

                # Make the request
                response = await client.create_document_schema(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.CreateDocumentSchemaRequest, dict]]):
                The request object. Request message for
                DocumentSchemaService.CreateDocumentSchema.
            parent (:class:`str`):
                Required. The parent name.
                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document_schema (:class:`google.cloud.contentwarehouse_v1.types.DocumentSchema`):
                Required. The document schema to
                create.

                This corresponds to the ``document_schema`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.types.DocumentSchema:
                A document schema used to define
                document structure.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, document_schema])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_schema_service.CreateDocumentSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if document_schema is not None:
            request.document_schema = document_schema

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_document_schema,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_document_schema(
        self,
        request: Optional[
            Union[document_schema_service.UpdateDocumentSchemaRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        document_schema: Optional[gcc_document_schema.DocumentSchema] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcc_document_schema.DocumentSchema:
        r"""Updates a Document Schema. Returns INVALID_ARGUMENT if the name
        of the Document Schema is non-empty and does not equal the
        existing name. Supports only appending new properties, adding
        new ENUM possible values, and updating the
        [EnumTypeOptions.validation_check_disabled][google.cloud.contentwarehouse.v1.EnumTypeOptions.validation_check_disabled]
        flag for ENUM possible values. Updating existing properties will
        result into INVALID_ARGUMENT.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_update_document_schema():
                # Create a client
                client = contentwarehouse_v1.DocumentSchemaServiceAsyncClient()

                # Initialize request argument(s)
                document_schema = contentwarehouse_v1.DocumentSchema()
                document_schema.display_name = "display_name_value"

                request = contentwarehouse_v1.UpdateDocumentSchemaRequest(
                    name="name_value",
                    document_schema=document_schema,
                )

                # Make the request
                response = await client.update_document_schema(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.UpdateDocumentSchemaRequest, dict]]):
                The request object. Request message for
                DocumentSchemaService.UpdateDocumentSchema.
            name (:class:`str`):
                Required. The name of the document schema to update.
                Format:
                projects/{project_number}/locations/{location}/documentSchemas/{document_schema_id}.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            document_schema (:class:`google.cloud.contentwarehouse_v1.types.DocumentSchema`):
                Required. The document schema to
                update with.

                This corresponds to the ``document_schema`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.types.DocumentSchema:
                A document schema used to define
                document structure.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, document_schema])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_schema_service.UpdateDocumentSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if document_schema is not None:
            request.document_schema = document_schema

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_document_schema,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_document_schema(
        self,
        request: Optional[
            Union[document_schema_service.GetDocumentSchemaRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> document_schema.DocumentSchema:
        r"""Gets a document schema. Returns NOT_FOUND if the document schema
        does not exist.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_get_document_schema():
                # Create a client
                client = contentwarehouse_v1.DocumentSchemaServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.GetDocumentSchemaRequest(
                    name="name_value",
                )

                # Make the request
                response = await client.get_document_schema(request=request)

                # Handle the response
                print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.GetDocumentSchemaRequest, dict]]):
                The request object. Request message for
                DocumentSchemaService.GetDocumentSchema.
            name (:class:`str`):
                Required. The name of the document
                schema to retrieve.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.types.DocumentSchema:
                A document schema used to define
                document structure.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_schema_service.GetDocumentSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_document_schema,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_document_schema(
        self,
        request: Optional[
            Union[document_schema_service.DeleteDocumentSchemaRequest, dict]
        ] = None,
        *,
        name: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes a document schema. Returns NOT_FOUND if the document
        schema does not exist. Returns BAD_REQUEST if the document
        schema has documents depending on it.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_delete_document_schema():
                # Create a client
                client = contentwarehouse_v1.DocumentSchemaServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.DeleteDocumentSchemaRequest(
                    name="name_value",
                )

                # Make the request
                await client.delete_document_schema(request=request)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.DeleteDocumentSchemaRequest, dict]]):
                The request object. Request message for
                DocumentSchemaService.DeleteDocumentSchema.
            name (:class:`str`):
                Required. The name of the document
                schema to delete.

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_schema_service.DeleteDocumentSchemaRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_document_schema,
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def list_document_schemas(
        self,
        request: Optional[
            Union[document_schema_service.ListDocumentSchemasRequest, dict]
        ] = None,
        *,
        parent: Optional[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: Union[float, object] = gapic_v1.method.DEFAULT,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListDocumentSchemasAsyncPager:
        r"""Lists document schemas.

        .. code-block:: python

            # This snippet has been automatically generated and should be regarded as a
            # code template only.
            # It will require modifications to work:
            # - It may require correct/in-range values for request initialization.
            # - It may require specifying regional endpoints when creating the service
            #   client as shown in:
            #   https://googleapis.dev/python/google-api-core/latest/client_options.html
            from google.cloud import contentwarehouse_v1

            async def sample_list_document_schemas():
                # Create a client
                client = contentwarehouse_v1.DocumentSchemaServiceAsyncClient()

                # Initialize request argument(s)
                request = contentwarehouse_v1.ListDocumentSchemasRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_document_schemas(request=request)

                # Handle the response
                async for response in page_result:
                    print(response)

        Args:
            request (Optional[Union[google.cloud.contentwarehouse_v1.types.ListDocumentSchemasRequest, dict]]):
                The request object. Request message for
                DocumentSchemaService.ListDocumentSchemas.
            parent (:class:`str`):
                Required. The parent, which owns this collection of
                document schemas. Format:
                projects/{project_number}/locations/{location}.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.contentwarehouse_v1.services.document_schema_service.pagers.ListDocumentSchemasAsyncPager:
                Response message for
                DocumentSchemaService.ListDocumentSchemas.
                Iterating over this object will yield
                results and resolve additional pages
                automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = document_schema_service.ListDocumentSchemasRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_document_schemas,
            default_retry=retries.Retry(
                initial=1.0,
                maximum=10.0,
                multiplier=1.3,
                predicate=retries.if_exception_type(
                    core_exceptions.ServiceUnavailable,
                ),
                deadline=60.0,
            ),
            default_timeout=60.0,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListDocumentSchemasAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
    gapic_version=package_version.__version__
)


__all__ = ("DocumentSchemaServiceAsyncClient",)
