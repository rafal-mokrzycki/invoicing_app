#!/usr/bin/env python
"""
Utilities to create a new ivoice
"""
import datetime as dt
import logging
import random
import smtplib
from pathlib import Path

import pandas as pd
from config_files.config import config


class InvoiceCreator:
    def __init__(
        self,
        invoice_type,
        issuer_tax_no,
        recipient_tax_no,
        positions,
        prices_net,
        tax_rates,
    ):
        if invoice_type in config["INVOICE_TYPES"]:
            self.invoice_type = invoice_type
        else:
            raise ValueError("Wrong invoice type")
        self.issuer_tax_no = issuer_tax_no
        self.recipient_tax_no = recipient_tax_no
        self.positions = positions
        self.prices_net = prices_net
        self.tax_rates = tax_rates
        self.prices_gross = [
            count_gross(i, j) for i, j in zip(self.prices_net, self.tax_rates)
        ]


def count_gross(amount, tax_rate):
    if tax_rate in config["TAX_RATES"]:
        return amount + amount * tax_rate
    else:
        raise ValueError("Wrong tax rate")
