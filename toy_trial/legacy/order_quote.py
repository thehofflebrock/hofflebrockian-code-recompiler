"""Legacy shipping quote behavior for the HCR v0.1 toy trial.

This implementation is intentionally repetitive. Its behavior, including
unfashionable edge handling, is the substrate to characterize. Do not treat the
file's appearance as evidence that a branch is accidental.
"""


def quote_order(
    subtotal_cents,
    item_count,
    region,
    *,
    member=False,
    expedited=False,
    promo_code=None,
):
    """Return the shipping charge in cents for one order."""

    if isinstance(subtotal_cents, bool) or not isinstance(subtotal_cents, int):
        raise TypeError("subtotal_cents must be a non-negative integer")
    if subtotal_cents < 0:
        raise ValueError("subtotal_cents must be a non-negative integer")

    if isinstance(item_count, bool) or not isinstance(item_count, int):
        raise TypeError("item_count must be an integer between 1 and 50")
    if item_count < 1 or item_count > 50:
        raise ValueError("item_count must be an integer between 1 and 50")

    if not isinstance(region, str):
        raise TypeError("region must be US, CA, or INTL")
    normalized_region = region.strip().upper()
    if normalized_region not in ("US", "CA", "INTL"):
        raise ValueError("region must be US, CA, or INTL")

    if not isinstance(member, bool):
        raise TypeError("member must be a boolean")
    if not isinstance(expedited, bool):
        raise TypeError("expedited must be a boolean")

    if promo_code is None:
        promo = None
    else:
        if not isinstance(promo_code, str):
            raise TypeError("promo_code must be a string or None")
        promo = promo_code.strip().upper()

    if normalized_region == "US":
        base = 599
        extra = 0

        if expedited:
            extra = 900

        if not expedited:
            if subtotal_cents >= 5000:
                base = 0

        if promo == "FREESHIP":
            if not expedited:
                if subtotal_cents >= 2500:
                    base = 0
        elif promo == "HALFSHIP":
            if base > 0:
                base = base // 2

        if member:
            if base > 0:
                base = base - 200
                if base < 0:
                    base = 0

        result = base + extra
        if item_count >= 10:
            result = result + 250
        return result

    if normalized_region == "CA":
        base = 1099
        extra = 0

        if expedited:
            extra = 1400

        if not expedited:
            if member:
                if subtotal_cents >= 7500:
                    base = 0

        if promo == "HALFSHIP":
            if base > 0:
                base = base // 2

        if member:
            if base > 0:
                base = base - 200
                if base < 0:
                    base = 0

        result = base + extra
        if item_count >= 10:
            result = result + 250
        return result

    if expedited:
        raise ValueError("expedited unavailable for INTL")

    base = 1799

    if promo == "HALFSHIP":
        if base > 0:
            base = base // 2

    if member:
        if base > 0:
            base = base - 200
            if base < 0:
                base = 0

    result = base
    if item_count >= 10:
        result = result + 250
    return result

