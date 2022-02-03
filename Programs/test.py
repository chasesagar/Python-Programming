
import uuid
import base64

def parse_csv_to_tmp_file(request):
    print(f"Request data is: {request}")

    tmp_file_name = f'sb-bulk-{str(uuid.uuid4())[:10]}.csv'
    try:

        with open(tmp_file_name, 'wb') as tmp_file:
            body = base64.b64decode(request)
            print(f"Request after decode: {body}, {type(body)}")
            if body[:1] == '"' and body[-1:] == '"':
                body = body[:-1][1:]
            print(f"After string changes: {body}")
            tmp_file.write(body)

        print(f"File : {tmp_file_name}")
    except Exception as e:
        print(e)

    return tmp_file_name

# Driver 
parse_csv_to_tmp_file("Zmlyc3RfbmFtZSxsYXN0X25hbWUscGhvbmVfbnVtYmVyLGVtYWlsLGdlbmRlcgpBZGFtLFphbXBhLCsxNDAxOTk5Mjg0Nyx4Y2lucmlsdnVpZW1vZmxpeG1Aa3ZocncuY29tLG1hbGUK")
