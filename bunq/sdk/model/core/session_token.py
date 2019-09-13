from abc import ABC

from bunq.sdk.model.core.bunq_model import BunqModel


class SessionToken(BunqModel, ABC):
    """
    :type _id_: int
    :type _created: str
    :type _updated: str
    :type _token: str
    """

    def __init__(self):
        self._id_ = None
        self._created = None
        self._updated = None
        self._token = None

    @property
    def id_(self):
        """
        :rtype: int
        """

        return self._id_

    @property
    def created(self):
        """
        :rtype: str
        """

        return self._created

    @property
    def updated(self):
        """
        :rtype: str
        """

        return self._updated

    @property
    def token(self):
        """
        :rtype: str
        """

        return self._token

    def is_all_field_none(self):
        if self.id_ is not None:
            return False

        if self.created is not None:
            return False

        if self.updated is not None:
            return False

        if self.token is not None:
            return False

        return True