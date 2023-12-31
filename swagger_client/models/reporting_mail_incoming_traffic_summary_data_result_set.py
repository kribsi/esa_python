# coding: utf-8

"""
    Secure Email Gateway API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportingMailIncomingTrafficSummaryDataResultSet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'blocked_dmarc': 'list[dict(str, object)]',
        'blocked_invalid_recipient': 'list[dict(str, object)]',
        'blocked_reputation': 'list[dict(str, object)]',
        'bulk_mail': 'list[dict(str, object)]',
        'detected_amp': 'list[dict(str, object)]',
        'detected_spam': 'list[dict(str, object)]',
        'detected_virus': 'list[dict(str, object)]',
        'ims_spam_increment_over_case': 'list[dict(str, object)]',
        'malicious_url': 'list[dict(str, object)]',
        'marketing_mail': 'list[dict(str, object)]',
        'social_mail': 'list[dict(str, object)]',
        'threat_content_filter': 'list[dict(str, object)]',
        'total_clean_recipients': 'list[dict(str, object)]',
        'total_graymail_recipients': 'list[dict(str, object)]',
        'total_recipients': 'list[dict(str, object)]',
        'total_threat_recipients': 'list[dict(str, object)]',
        'verif_decrypt_fail': 'list[dict(str, object)]',
        'verif_decrypt_success': 'list[dict(str, object)]',
        'detected_spam_suspect': 'list[dict(str, object)]',
        'detected_spam_certain': 'list[dict(str, object)]',
        'failed_spf': 'list[dict(str, object)]',
        'failed_dkim': 'list[dict(str, object)]',
        'total_spoofed_emails': 'list[dict(str, object)]',
        'total_mailbox_auto_remediated_recipients': 'list[dict(str, object)]',
        'detected_virus_per_msg': 'list[dict(str, object)]'
    }

    attribute_map = {
        'blocked_dmarc': 'blocked_dmarc',
        'blocked_invalid_recipient': 'blocked_invalid_recipient',
        'blocked_reputation': 'blocked_reputation',
        'bulk_mail': 'bulk_mail',
        'detected_amp': 'detected_amp',
        'detected_spam': 'detected_spam',
        'detected_virus': 'detected_virus',
        'ims_spam_increment_over_case': 'ims_spam_increment_over_case',
        'malicious_url': 'malicious_url',
        'marketing_mail': 'marketing_mail',
        'social_mail': 'social_mail',
        'threat_content_filter': 'threat_content_filter',
        'total_clean_recipients': 'total_clean_recipients',
        'total_graymail_recipients': 'total_graymail_recipients',
        'total_recipients': 'total_recipients',
        'total_threat_recipients': 'total_threat_recipients',
        'verif_decrypt_fail': 'verif_decrypt_fail',
        'verif_decrypt_success': 'verif_decrypt_success',
        'detected_spam_suspect': 'detected_spam_suspect',
        'detected_spam_certain': 'detected_spam_certain',
        'failed_spf': 'failed_spf',
        'failed_dkim': 'failed_dkim',
        'total_spoofed_emails': 'total_spoofed_emails',
        'total_mailbox_auto_remediated_recipients': 'total_mailbox_auto_remediated_recipients',
        'detected_virus_per_msg': 'detected_virus_per_msg'
    }

    def __init__(self, blocked_dmarc=None, blocked_invalid_recipient=None, blocked_reputation=None, bulk_mail=None, detected_amp=None, detected_spam=None, detected_virus=None, ims_spam_increment_over_case=None, malicious_url=None, marketing_mail=None, social_mail=None, threat_content_filter=None, total_clean_recipients=None, total_graymail_recipients=None, total_recipients=None, total_threat_recipients=None, verif_decrypt_fail=None, verif_decrypt_success=None, detected_spam_suspect=None, detected_spam_certain=None, failed_spf=None, failed_dkim=None, total_spoofed_emails=None, total_mailbox_auto_remediated_recipients=None, detected_virus_per_msg=None):  # noqa: E501
        """ReportingMailIncomingTrafficSummaryDataResultSet - a model defined in Swagger"""  # noqa: E501
        self._blocked_dmarc = None
        self._blocked_invalid_recipient = None
        self._blocked_reputation = None
        self._bulk_mail = None
        self._detected_amp = None
        self._detected_spam = None
        self._detected_virus = None
        self._ims_spam_increment_over_case = None
        self._malicious_url = None
        self._marketing_mail = None
        self._social_mail = None
        self._threat_content_filter = None
        self._total_clean_recipients = None
        self._total_graymail_recipients = None
        self._total_recipients = None
        self._total_threat_recipients = None
        self._verif_decrypt_fail = None
        self._verif_decrypt_success = None
        self._detected_spam_suspect = None
        self._detected_spam_certain = None
        self._failed_spf = None
        self._failed_dkim = None
        self._total_spoofed_emails = None
        self._total_mailbox_auto_remediated_recipients = None
        self._detected_virus_per_msg = None
        self.discriminator = None
        if blocked_dmarc is not None:
            self.blocked_dmarc = blocked_dmarc
        if blocked_invalid_recipient is not None:
            self.blocked_invalid_recipient = blocked_invalid_recipient
        if blocked_reputation is not None:
            self.blocked_reputation = blocked_reputation
        if bulk_mail is not None:
            self.bulk_mail = bulk_mail
        if detected_amp is not None:
            self.detected_amp = detected_amp
        if detected_spam is not None:
            self.detected_spam = detected_spam
        if detected_virus is not None:
            self.detected_virus = detected_virus
        if ims_spam_increment_over_case is not None:
            self.ims_spam_increment_over_case = ims_spam_increment_over_case
        if malicious_url is not None:
            self.malicious_url = malicious_url
        if marketing_mail is not None:
            self.marketing_mail = marketing_mail
        if social_mail is not None:
            self.social_mail = social_mail
        if threat_content_filter is not None:
            self.threat_content_filter = threat_content_filter
        if total_clean_recipients is not None:
            self.total_clean_recipients = total_clean_recipients
        if total_graymail_recipients is not None:
            self.total_graymail_recipients = total_graymail_recipients
        if total_recipients is not None:
            self.total_recipients = total_recipients
        if total_threat_recipients is not None:
            self.total_threat_recipients = total_threat_recipients
        if verif_decrypt_fail is not None:
            self.verif_decrypt_fail = verif_decrypt_fail
        if verif_decrypt_success is not None:
            self.verif_decrypt_success = verif_decrypt_success
        if detected_spam_suspect is not None:
            self.detected_spam_suspect = detected_spam_suspect
        if detected_spam_certain is not None:
            self.detected_spam_certain = detected_spam_certain
        if failed_spf is not None:
            self.failed_spf = failed_spf
        if failed_dkim is not None:
            self.failed_dkim = failed_dkim
        if total_spoofed_emails is not None:
            self.total_spoofed_emails = total_spoofed_emails
        if total_mailbox_auto_remediated_recipients is not None:
            self.total_mailbox_auto_remediated_recipients = total_mailbox_auto_remediated_recipients
        if detected_virus_per_msg is not None:
            self.detected_virus_per_msg = detected_virus_per_msg

    @property
    def blocked_dmarc(self):
        """Gets the blocked_dmarc of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The blocked_dmarc of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._blocked_dmarc

    @blocked_dmarc.setter
    def blocked_dmarc(self, blocked_dmarc):
        """Sets the blocked_dmarc of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param blocked_dmarc: The blocked_dmarc of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._blocked_dmarc = blocked_dmarc

    @property
    def blocked_invalid_recipient(self):
        """Gets the blocked_invalid_recipient of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The blocked_invalid_recipient of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._blocked_invalid_recipient

    @blocked_invalid_recipient.setter
    def blocked_invalid_recipient(self, blocked_invalid_recipient):
        """Sets the blocked_invalid_recipient of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param blocked_invalid_recipient: The blocked_invalid_recipient of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._blocked_invalid_recipient = blocked_invalid_recipient

    @property
    def blocked_reputation(self):
        """Gets the blocked_reputation of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The blocked_reputation of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._blocked_reputation

    @blocked_reputation.setter
    def blocked_reputation(self, blocked_reputation):
        """Sets the blocked_reputation of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param blocked_reputation: The blocked_reputation of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._blocked_reputation = blocked_reputation

    @property
    def bulk_mail(self):
        """Gets the bulk_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The bulk_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._bulk_mail

    @bulk_mail.setter
    def bulk_mail(self, bulk_mail):
        """Sets the bulk_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param bulk_mail: The bulk_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._bulk_mail = bulk_mail

    @property
    def detected_amp(self):
        """Gets the detected_amp of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_amp of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_amp

    @detected_amp.setter
    def detected_amp(self, detected_amp):
        """Sets the detected_amp of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_amp: The detected_amp of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_amp = detected_amp

    @property
    def detected_spam(self):
        """Gets the detected_spam of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_spam of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_spam

    @detected_spam.setter
    def detected_spam(self, detected_spam):
        """Sets the detected_spam of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_spam: The detected_spam of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_spam = detected_spam

    @property
    def detected_virus(self):
        """Gets the detected_virus of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_virus of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_virus

    @detected_virus.setter
    def detected_virus(self, detected_virus):
        """Sets the detected_virus of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_virus: The detected_virus of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_virus = detected_virus

    @property
    def ims_spam_increment_over_case(self):
        """Gets the ims_spam_increment_over_case of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The ims_spam_increment_over_case of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._ims_spam_increment_over_case

    @ims_spam_increment_over_case.setter
    def ims_spam_increment_over_case(self, ims_spam_increment_over_case):
        """Sets the ims_spam_increment_over_case of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param ims_spam_increment_over_case: The ims_spam_increment_over_case of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._ims_spam_increment_over_case = ims_spam_increment_over_case

    @property
    def malicious_url(self):
        """Gets the malicious_url of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The malicious_url of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._malicious_url

    @malicious_url.setter
    def malicious_url(self, malicious_url):
        """Sets the malicious_url of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param malicious_url: The malicious_url of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._malicious_url = malicious_url

    @property
    def marketing_mail(self):
        """Gets the marketing_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The marketing_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._marketing_mail

    @marketing_mail.setter
    def marketing_mail(self, marketing_mail):
        """Sets the marketing_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param marketing_mail: The marketing_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._marketing_mail = marketing_mail

    @property
    def social_mail(self):
        """Gets the social_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The social_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._social_mail

    @social_mail.setter
    def social_mail(self, social_mail):
        """Sets the social_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param social_mail: The social_mail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._social_mail = social_mail

    @property
    def threat_content_filter(self):
        """Gets the threat_content_filter of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The threat_content_filter of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._threat_content_filter

    @threat_content_filter.setter
    def threat_content_filter(self, threat_content_filter):
        """Sets the threat_content_filter of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param threat_content_filter: The threat_content_filter of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._threat_content_filter = threat_content_filter

    @property
    def total_clean_recipients(self):
        """Gets the total_clean_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_clean_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_clean_recipients

    @total_clean_recipients.setter
    def total_clean_recipients(self, total_clean_recipients):
        """Sets the total_clean_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_clean_recipients: The total_clean_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_clean_recipients = total_clean_recipients

    @property
    def total_graymail_recipients(self):
        """Gets the total_graymail_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_graymail_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_graymail_recipients

    @total_graymail_recipients.setter
    def total_graymail_recipients(self, total_graymail_recipients):
        """Sets the total_graymail_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_graymail_recipients: The total_graymail_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_graymail_recipients = total_graymail_recipients

    @property
    def total_recipients(self):
        """Gets the total_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_recipients

    @total_recipients.setter
    def total_recipients(self, total_recipients):
        """Sets the total_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_recipients: The total_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_recipients = total_recipients

    @property
    def total_threat_recipients(self):
        """Gets the total_threat_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_threat_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_threat_recipients

    @total_threat_recipients.setter
    def total_threat_recipients(self, total_threat_recipients):
        """Sets the total_threat_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_threat_recipients: The total_threat_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_threat_recipients = total_threat_recipients

    @property
    def verif_decrypt_fail(self):
        """Gets the verif_decrypt_fail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The verif_decrypt_fail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._verif_decrypt_fail

    @verif_decrypt_fail.setter
    def verif_decrypt_fail(self, verif_decrypt_fail):
        """Sets the verif_decrypt_fail of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param verif_decrypt_fail: The verif_decrypt_fail of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._verif_decrypt_fail = verif_decrypt_fail

    @property
    def verif_decrypt_success(self):
        """Gets the verif_decrypt_success of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The verif_decrypt_success of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._verif_decrypt_success

    @verif_decrypt_success.setter
    def verif_decrypt_success(self, verif_decrypt_success):
        """Sets the verif_decrypt_success of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param verif_decrypt_success: The verif_decrypt_success of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._verif_decrypt_success = verif_decrypt_success

    @property
    def detected_spam_suspect(self):
        """Gets the detected_spam_suspect of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_spam_suspect of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_spam_suspect

    @detected_spam_suspect.setter
    def detected_spam_suspect(self, detected_spam_suspect):
        """Sets the detected_spam_suspect of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_spam_suspect: The detected_spam_suspect of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_spam_suspect = detected_spam_suspect

    @property
    def detected_spam_certain(self):
        """Gets the detected_spam_certain of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_spam_certain of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_spam_certain

    @detected_spam_certain.setter
    def detected_spam_certain(self, detected_spam_certain):
        """Sets the detected_spam_certain of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_spam_certain: The detected_spam_certain of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_spam_certain = detected_spam_certain

    @property
    def failed_spf(self):
        """Gets the failed_spf of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The failed_spf of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._failed_spf

    @failed_spf.setter
    def failed_spf(self, failed_spf):
        """Sets the failed_spf of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param failed_spf: The failed_spf of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._failed_spf = failed_spf

    @property
    def failed_dkim(self):
        """Gets the failed_dkim of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The failed_dkim of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._failed_dkim

    @failed_dkim.setter
    def failed_dkim(self, failed_dkim):
        """Sets the failed_dkim of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param failed_dkim: The failed_dkim of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._failed_dkim = failed_dkim

    @property
    def total_spoofed_emails(self):
        """Gets the total_spoofed_emails of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_spoofed_emails of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_spoofed_emails

    @total_spoofed_emails.setter
    def total_spoofed_emails(self, total_spoofed_emails):
        """Sets the total_spoofed_emails of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_spoofed_emails: The total_spoofed_emails of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_spoofed_emails = total_spoofed_emails

    @property
    def total_mailbox_auto_remediated_recipients(self):
        """Gets the total_mailbox_auto_remediated_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The total_mailbox_auto_remediated_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._total_mailbox_auto_remediated_recipients

    @total_mailbox_auto_remediated_recipients.setter
    def total_mailbox_auto_remediated_recipients(self, total_mailbox_auto_remediated_recipients):
        """Sets the total_mailbox_auto_remediated_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param total_mailbox_auto_remediated_recipients: The total_mailbox_auto_remediated_recipients of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._total_mailbox_auto_remediated_recipients = total_mailbox_auto_remediated_recipients

    @property
    def detected_virus_per_msg(self):
        """Gets the detected_virus_per_msg of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501


        :return: The detected_virus_per_msg of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :rtype: list[dict(str, object)]
        """
        return self._detected_virus_per_msg

    @detected_virus_per_msg.setter
    def detected_virus_per_msg(self, detected_virus_per_msg):
        """Sets the detected_virus_per_msg of this ReportingMailIncomingTrafficSummaryDataResultSet.


        :param detected_virus_per_msg: The detected_virus_per_msg of this ReportingMailIncomingTrafficSummaryDataResultSet.  # noqa: E501
        :type: list[dict(str, object)]
        """

        self._detected_virus_per_msg = detected_virus_per_msg

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ReportingMailIncomingTrafficSummaryDataResultSet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ReportingMailIncomingTrafficSummaryDataResultSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
