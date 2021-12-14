CHILD_ATTENDANCE_MODE_OPTIONS = {
	"onBoarding": "child_status",
    "offBoarding": "child_offboarding_status"
}

def valid(mode):
    request_string_props = ["child_id","route_type","route_id","stop_id", CHILD_ATTENDANCE_MODE_OPTIONS[mode]]
    
    print(request_string_props)
    
    
valid("offBoarding")