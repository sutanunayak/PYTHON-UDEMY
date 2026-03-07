def serve_chai(flavour):
    try:
        print(f"Preparing {flavour} ...")
        if flavour == "unknown":
            raise ValueError("we don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavour} is served")
    finally:
        print("Next customer please")

serve_chai("masala chai")
serve_chai("unknown")