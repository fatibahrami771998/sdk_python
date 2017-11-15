import json
import os

from tests import bunq_test
from bunq.sdk.model.generated import object_
from bunq.sdk.model.generated import endpoint
from bunq.sdk.json.converter import json_to_class


class TestNotificationUrl(bunq_test.BunqSdkTestCase):
    # Getter string constants
    # Assertion errors
    _ASSERT_SHOULD_NOT_REACH_THIS_CODE_ERROR = \
        'Something super weird just happen'
    _ASSERT_JSON_DECODE_ERROR = \
        'Might be that the JSON file is not a valid json.'
    _ASSERT_OBJECT_IS_NULL_ERROR = 'Object seems to be null.'
    _GETTER_PAYMENT = 'Payment'
    _GETTER_BUNQ_ME_TAB = 'BunqMeTab'
    _GETTER_CHAT_MESSAGE_ANNOUNCEMENT = 'ChatMessageAnnouncement'
    _GETTER_DRAFT_PAYMENT = 'DraftPayment'
    _GETTER_MASTER_CARD_ACTION = 'MasterCardAction'
    _GETTER_MONETARY_ACCOUNT_BANK = 'MonetaryAccountBank'
    _GETTER_PAYMENT_BATCH = 'PaymentBatch'
    _GETTER_REQUEST_INQUIRY = 'RequestInquiry'
    _GETTER_REQUEST_RESPONSE = 'RequestResponse'
    _GETTER_SCHEDULE_PAYMENT = 'ScheduledPayment'
    _GETTER_SCHEDULE_INSTANCE = 'ScheduledInstance'
    _GETTER_SHARE_INVITE_BANK_INQUIRY = 'ShareInviteBankInquiry'
    _GETTER_SHARE_INVITE_BANK_RESPONSE = 'ShareInviteBankResponse'

    # Model json paths constants.
    BASE_PATH_JSON_MODEL = '../../../assets/NotficationUrlJsons'
    JSON_PATH_MUTATION_MODEL = BASE_PATH_JSON_MODEL + '/Mutation.json'
    JSON_PATH_BUNQ_ME_TAB_MODEL = BASE_PATH_JSON_MODEL + '/BunqMeTab.json'
    JSON_PATH_CHAT_MESSAGE_ANNOUNCEMENT_MODEL = \
        BASE_PATH_JSON_MODEL + '/ChatMessageAnnouncement.json'
    JSON_PATH_DRAFT_PAYMENT_MODEL = BASE_PATH_JSON_MODEL + '/DraftPayment.json'
    JSON_PATH_MASTER_CARD_ACTION_MODEL = \
        BASE_PATH_JSON_MODEL + '/MasterCardAction.json'
    JSON_PATH_MONETARY_ACCOUNT_BANK_MODEL = \
        BASE_PATH_JSON_MODEL + '/MonetaryAccountBank.json'
    JSON_PATH_PAYMENT_BATCH_MODEL = \
        BASE_PATH_JSON_MODEL + '/PaymentBatch.json'
    JSON_PATH_REQUEST_INQUIRY_MODEL = \
        BASE_PATH_JSON_MODEL + '/RequestInquiry.json'
    JSON_PATH_REQUEST_RESPONSE_MODEL = \
        BASE_PATH_JSON_MODEL + '/RequestResponse.json'
    JSON_PATH_SCHEDULE_PAYMENT_MODEL = \
        BASE_PATH_JSON_MODEL + '/ScheduledPayment.json'
    JSON_PATH_SCHEDULE_INSTANCE_MODEL = \
        BASE_PATH_JSON_MODEL + '/ScheduledInstance.json'
    JSON_PATH_SHARE_INVITE_BANK_INQUIRY_MODEL = \
        BASE_PATH_JSON_MODEL + '/ShareInviteBankInquiry.json'
    JSON_PATH_SHARE_INVITE_BANK_RESPONSE_MODEL = \
        BASE_PATH_JSON_MODEL + '/ShareInviteBankResponse.json'

    # Model root key.
    _KEY_NOTIFICATION_URL_MODEL = 'NotificationUrl'

    def execute_notification_url_test(self,
                                      file_path,
                                      class_name,
                                      getter_name):
        """
        :type file_path: str
        :type class_name: str
        :type getter_name: str

        :return: None
        """

        notification_url = self.getNotificationUrl(file_path)
        self.assertIsNotNone(notification_url)
        self.assertIsNotNone(notification_url.object_)

        expected_model = getattr(notification_url.object_, getter_name)
        referenced_model = notification_url.object_.get_referenced_object()

        self.assertIsNotNone(expected_model)
        self.assertIsNotNone(referenced_model)
        self.assertTrue(
            self.assertInstanceOfReferencedObject(
                referenced_model,
                class_name
            )
            or
            self.assertInstanceOfReferencedEndpoint(
                referenced_model,
                class_name
            )
        )

    @staticmethod
    def assertInstanceOfReferencedObject(referenced_model, class_name):
        try:
            return isinstance(referenced_model, getattr(object_, class_name))
        except AttributeError:
            return False

    @staticmethod
    def assertInstanceOfReferencedEndpoint(referenced_model, class_name):
        try:
            return isinstance(referenced_model, getattr(endpoint, class_name))
        except AttributeError:
            return False

    def getNotificationUrl(self, file_path):
        """
        :type file_path: str

        :rtype: object_.NotificationUrl
        """

        base_path = os.path.dirname(__file__)
        file_path = os.path.abspath(os.path.join(base_path, file_path))

        with open(file_path, 'r') as f:
            json_string = f.read()
            json_object = json.loads(json_string)
            json_string = json.dumps(json_object[
                                         self._KEY_NOTIFICATION_URL_MODEL
                                     ])

            self.assertTrue(
                self._KEY_NOTIFICATION_URL_MODEL in json_object
            )

            return json_to_class(
                object_.NotificationUrl,
                json_string
            )

    def test_mutation_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MUTATION_MODEL,
            endpoint.Payment.__name__,
            self._GETTER_PAYMENT
        )

    def test_bunq_me_tab_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_BUNQ_ME_TAB_MODEL,
            endpoint.BunqMeTab.__name__,
            self._GETTER_BUNQ_ME_TAB
        )

    def test_chat_message_announcement_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_CHAT_MESSAGE_ANNOUNCEMENT_MODEL,
            endpoint.ChatMessageAnnouncement.__name__,
            self._GETTER_CHAT_MESSAGE_ANNOUNCEMENT
        )

    def test_draft_payment_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_DRAFT_PAYMENT_MODEL,
            endpoint.DraftPayment.__name__,
            self._GETTER_DRAFT_PAYMENT
        )

    def test_mastercard_action(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MASTER_CARD_ACTION_MODEL,
            endpoint.MasterCardAction.__name__,
            self._GETTER_MASTER_CARD_ACTION
        )

    def test_monetary_account_bank_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_MONETARY_ACCOUNT_BANK_MODEL,
            endpoint.MonetaryAccountBank.__name__,
            self._GETTER_MONETARY_ACCOUNT_BANK
        )

    def test_payment_batch_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_PAYMENT_BATCH_MODEL,
            endpoint.PaymentBatch.__name__,
            self._GETTER_PAYMENT_BATCH
        )

    def test_request_inquiry_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_REQUEST_INQUIRY_MODEL,
            endpoint.RequestInquiry.__name__,
            self._GETTER_REQUEST_INQUIRY
        )

    def test_request_response_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_REQUEST_RESPONSE_MODEL,
            endpoint.RequestResponse.__name__,
            self._GETTER_REQUEST_RESPONSE
        )

    def test_scheduled_payment_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SCHEDULE_PAYMENT_MODEL,
            endpoint.SchedulePayment.__name__,
            self._GETTER_SCHEDULE_PAYMENT
        )

    def test_scheduled_instance_model(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SCHEDULE_INSTANCE_MODEL,
            endpoint.ScheduleInstance.__name__,
            self._GETTER_SCHEDULE_INSTANCE
        )

    def test_share_invite_bank_inquiry(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SHARE_INVITE_BANK_INQUIRY_MODEL,
            endpoint.ShareInviteBankInquiry.__name__,
            self._GETTER_SHARE_INVITE_BANK_INQUIRY
        )

    def test_share_invite_bank_response(self):
        self.execute_notification_url_test(
            self.JSON_PATH_SHARE_INVITE_BANK_RESPONSE_MODEL,
            endpoint.ShareInviteBankResponse.__name__,
            self._GETTER_SHARE_INVITE_BANK_RESPONSE
        )
