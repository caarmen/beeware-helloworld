# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Any, Dict, Optional, Union

from .async_base_client import AsyncBaseClient
from .base_model import UNSET, UnsetType
from .film_query import FilmQuery


def gql(q: str) -> str:
    return q


class Client(AsyncBaseClient):
    async def film_query(
        self, id: Union[Optional[str], UnsetType] = UNSET, **kwargs: Any
    ) -> FilmQuery:
        query = gql(
            """
            query FilmQuery($id: ID) {
              film(id: $id) {
                title
                director
                releaseDate
              }
            }
            """
        )
        variables: Dict[str, object] = {"id": id}
        response = await self.execute(query=query, variables=variables, **kwargs)
        data = self.get_data(response)
        return FilmQuery.model_validate(data)