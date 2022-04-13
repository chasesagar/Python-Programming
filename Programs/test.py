import uuid
import base64


def parse_csv_to_tmp_file(request):
    print(f"Request data is: {request}")

    tmp_file_name = f"sb-bulk-{str(uuid.uuid4())[:10]}.csv"
    try:

        with open(tmp_file_name, "wb") as tmp_file:
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
parse_csv_to_tmp_file(
    "Zmlyc3RfbmFtZSxsYXN0X25hbWUscGhvbmVfbnVtYmVyLGVtYWlsLGdlbmRlcgpBZGFtLFphbXBhLCsxNDAxOTk5Mjg0Nyx4Y2lucmlsdnVpZW1vZmxpeG1Aa3ZocncuY29tLG1hbGUK"
)

{
    "Username": "75d41f84-9538-4d27-ad7e-3f425ce97cc9",
    "UserAttributes": [
        {"Name": "sub", "Value": "75d41f84-9538-4d27-ad7e-3f425ce97cc9"},
        {"Name": "address", "Value": "Demo St, NY"},
        {"Name": "email_verified", "Value": "true"},
        {"Name": "gender", "Value": "male"},
        {"Name": "name", "Value": "demo@spotbus.us"},
        {"Name": "phone_number_verified", "Value": "false"},
        {"Name": "phone_number", "Value": "+19999999999"},
        {"Name": "given_name", "Value": "Demo"},
        {"Name": "family_name", "Value": "Customer"},
        {"Name": "email", "Value": "demo@spotbus.us"},
    ],
    "UserCreateDate": datetime.datetime(2021, 4, 22, 15, 29, 4, 901000, tzinfo=tzlocal()),
    "UserLastModifiedDate": datetime.datetime(2021, 4, 22, 15, 29, 25, 643000, tzinfo=tzlocal()),
    "Enabled": True,
    "UserStatus": "CONFIRMED",
    "ResponseMetadata": {
        "RequestId": "daefccb7-25ea-482b-ae0b-21ae4fb15f62",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "date": "Tue, 29 Mar 2022 14:48:28 GMT",
            "content-type": "application/x-amz-json-1.1",
            "content-length": "621",
            "connection": "keep-alive",
            "x-amzn-requestid": "daefccb7-25ea-482b-ae0b-21ae4fb15f62",
        },
        "RetryAttempts": 0,
    },
}
