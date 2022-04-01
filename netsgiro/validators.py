"""Custom validators for :mod:`attrs`."""
from datetime import date, datetime, timedelta
from typing import NoReturn

from attr.validators import instance_of

from netsgiro.utils import OSLO_TZ, get_minimum_due_date


def str_of_length(length):
    """Validate that the value is a string of the given length."""

    def validator(instance, attribute, value):
        instance_of(str)(instance, attribute, value)
        if len(value) != length:
            raise ValueError(
                '{0.name} must be exactly {1} chars, got {2!r}'.format(
                    attribute, length, value
                )
            )

    return validator


def str_of_max_length(length):
    """Validate that the value is a string with a max length."""

    def validator(instance, attribute, value):
        instance_of(str)(instance, attribute, value)
        if len(value) > length:
            raise ValueError(
                '{0.name} must be at most {1} chars, '
                'got {2!r} which is {3} chars'.format(
                    attribute, length, value, len(value)
                )
            )

    return validator


def validate_due_date(value: date) -> NoReturn:
    """Make sure payment request dates are gt the minimum allowed date."""
    now = datetime.now(tz=OSLO_TZ)

    if value < get_minimum_due_date(now=now):
        raise ValueError(
            'The minimum due date of a transaction is today + 4 calendar days.'
            ' OCR files with due dates earlier than this will be rejected when'
            ' submitted.'
        )

    if value > (now + timedelta(days=365)).date():
        raise ValueError(
            'The maximum due date of a transaction is 12 months into the future.'
            ' OCR files with due dates later than this will be rejected when'
            ' submitted.'
        )
