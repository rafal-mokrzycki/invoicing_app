#!/usr/bin/env python
"""
Utilities to create a new ivoice
"""
import datetime
import logging
import random
import smtplib
from pathlib import Path

import numpy as np
import pandas as pd
from config_files.config import config
from fpdf import FPDF

CURRENCY = config["CURRENCY"]


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
            calculate_gross(i, j) for i, j in zip(self.prices_net, self.tax_rates)
        ]
        self.sum_net = calculate_sum(self.prices_net)
        self.sum_gross = calculate_sum(self.prices_gross)
        self.sum_tax = self.sum_gross - self.sum_net

    def show_invoice(self):
        string1 = f"""
        {'='*60}
        {self.invoice_type.upper()} INVOICE

        Issuer tax no.: {self.issuer_tax_no}
        Recipient tax no.: {self.recipient_tax_no}

        Position\tNet amount\tTax rate\tGross amount
        """
        string2 = ""
        # string2 = f"""
        # {[(i, j, k, l) for i, j, k, l in zip(self.positions, self.prices_net, self.tax_rates, self.prices_gross)]}
        # """
        string3 = f"""
        Net sum: {self.sum_net}
        Tax sum: {self.sum_tax}
        TOTAL SUM: {self.sum_gross}
        {'='*60}"""

        print(string1, string2, string3, sep="\n\n")

    def save_to_pdf(self):
        """Saves invoice as a pdf file"""
        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()

        # Set invoice name
        pdf.set_font("Times", "B", 16)
        pdf.cell(0, 16, txt=f"{self.invoice_type.upper()} INVOICE", ln=2, align="L")

        # Issuer and recipient data
        pdf.set_font("Times", "", 12)
        pdf.cell(200, 10, txt=f"Issuer tax no.: {self.issuer_tax_no}", ln=2, align="l")
        pdf.cell(
            200, 10, txt=f"Recipient tax no.: {self.recipient_tax_no}", ln=2, align="l"
        )
        # Positions of an invoice
        pdf.set_font("Times", "B", 12)
        for size, elem in zip(
            [100, 30, 30, 30], ["Position", "Net amount", "Tax rate", "Gross amount"]
        ):
            pdf.cell(size, 8, txt=elem, ln=0, border=1)
        pdf.cell(10, 8, txt="", ln=1)
        pdf.set_font("Times", "", 12)
        for position in range(len(self.positions)):
            for size, elem in zip(
                [100, 30, 30, 30],
                [self.positions, self.prices_net, self.tax_rates, self.prices_gross],
            ):
                pdf.cell(size, 10, txt=str(elem[position]), ln=0, border=1)
            pdf.cell(10, 10, txt="", ln=1)

        # Net, tax and gross amount
        pdf.cell(200, 10, txt=f"Net sum: {self.sum_net} {CURRENCY}", ln=2, align="R")
        pdf.cell(200, 10, txt=f"Tax sum: {self.sum_tax} {CURRENCY}", ln=2, align="R")
        pdf.set_font("Times", "B", 12)
        pdf.cell(200, 10, txt=f"TOTAL SUM: {self.sum_gross} {CURRENCY}", ln=2, align="R")

        pdf.output(
            f"{self.invoice_type.replace(' ','_')}_invoice_{datetime.datetime.now().strftime('%Y%m%d')}.pdf"
        )


def calculate_gross(amount, tax_rate):
    if tax_rate in config["TAX_RATES"]:
        return float(amount + amount * tax_rate)
    else:
        raise ValueError("Wrong tax rate")


def calculate_sum(iterable):
    return float(np.sum(iterable))