def is_number(v):
    try:
        float(v)
        return True
    except:
        return False