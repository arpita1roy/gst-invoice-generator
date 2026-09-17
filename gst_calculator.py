def calculate_gst(amount, gst_rate, interstate=False):
    """
    Calculate GST for an invoice amount.

    For intrastate transactions:
        GST is divided into CGST and SGST.

    For interstate transactions:
        GST is applied as IGST.
    """

    gst_amount = amount * (gst_rate / 100)

    if interstate:
        cgst = 0
        sgst = 0
        igst = gst_amount
    else:
        cgst = gst_amount / 2
        sgst = gst_amount / 2
        igst = 0

    total_amount = amount + gst_amount

    return {
        "base_amount": round(amount, 2),
        "gst_rate": gst_rate,
        "cgst": round(cgst, 2),
        "sgst": round(sgst, 2),
        "igst": round(igst, 2),
        "gst_amount": round(gst_amount, 2),
        "total_amount": round(total_amount, 2)
    }


if __name__ == "__main__":
    result = calculate_gst(1000, 18)

    print("GST Invoice Calculation")
    print("-----------------------")
    print(f"Base Amount : ₹{result['base_amount']}")
    print(f"GST Rate    : {result['gst_rate']}%")
    print(f"CGST        : ₹{result['cgst']}")
    print(f"SGST        : ₹{result['sgst']}")
    print(f"Total GST   : ₹{result['gst_amount']}")
    print(f"Total Amount : ₹{result['total_amount']}")
