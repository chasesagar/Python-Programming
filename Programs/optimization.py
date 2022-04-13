import json

route = {
    "super_admin_user_id": "75d41f84-9538-4d27-ad7e-3f425ce97cc9",
    "jobId": "1b57c6ef-d",
    "type": "ROUTE_PLANNER",
    "status": "COMPLETED",
    "total_items": 4,
    "completed_items": 4,
    "failed_items": 0,
    "created_by": "75d41f84-9538-4d27-ad7e-3f425ce97cc9",
    "creation_timestamp": 1644223433,
    "last_updated_timestamp": 1644250818,
    "request_file_path": [
        {
            "driver_name": "Test1 Driver",
            "start_time": 0,
            "driver_id": "e073d8a9-10fc-4afc-9670-850231bec2e6",
            "agent_id": "16406311735ec9713c",
            "distance": 10556,
            "school_id": "BOS2",
            "end_time": 2889,
            "time": 2889,
            "preferred_time_info": {
                "time_range_pm": {
                    "end_time": "05:00:00",
                    "time_window": 7200,
                    "start_time": "03:00:00",
                },
                "time_range_am": {
                    "end_time": "09:00:00",
                    "time_window": 10800,
                    "start_time": "06:00:00",
                },
            },
            "waypoints": [
                {
                    "duration": 0,
                    "start_time": 0,
                    "next_leg_index": 0,
                    "original_location": ["42.270017", "-71.623672"],
                    "location": ["42.270017", "-71.623672"],
                    "actions": [
                        {
                            "duration": 0,
                            "index": 0,
                            "start_time": 0,
                            "type": "start",
                            "waypoint_index": 0,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 33,
                    "next_leg_index": 1,
                    "original_location": ["42.2705644", "-71.6212994"],
                    "prev_leg_index": 0,
                    "location": ["42.270564", "-71.621299"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 33,
                            "job_index": 24,
                            "job_id": "163683624745e9f753",
                            "index": 1,
                            "type": "job",
                            "waypoint_index": 1,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 143,
                    "next_leg_index": 2,
                    "original_location": ["42.2703619", "-71.617174"],
                    "prev_leg_index": 1,
                    "location": ["42.270362", "-71.617174"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 143,
                            "job_index": 22,
                            "job_id": "1636836421dbf81ea2",
                            "index": 2,
                            "type": "job",
                            "waypoint_index": 2,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 230,
                    "next_leg_index": 3,
                    "original_location": ["42.2697458", "-71.6152395"],
                    "prev_leg_index": 2,
                    "location": ["42.269746", "-71.61524"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 230,
                            "job_index": 21,
                            "job_id": "1631295451b1e2867c",
                            "index": 3,
                            "type": "job",
                            "waypoint_index": 3,
                        }
                    ],
                },
                {
                    "duration": 180,
                    "start_time": 354,
                    "next_leg_index": 4,
                    "original_location": ["42.2681683", "-71.6163167"],
                    "prev_leg_index": 3,
                    "location": ["42.268168", "-71.616317"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 354,
                            "job_index": 19,
                            "job_id": "162879366623895afd",
                            "index": 4,
                            "type": "job",
                            "waypoint_index": 4,
                        },
                        {
                            "duration": 60,
                            "start_time": 414,
                            "job_index": 18,
                            "job_id": "16368364291d8d7598",
                            "index": 5,
                            "type": "job",
                            "waypoint_index": 4,
                        },
                        {
                            "duration": 60,
                            "start_time": 474,
                            "job_index": 17,
                            "job_id": "163819362166c812e8",
                            "index": 6,
                            "type": "job",
                            "waypoint_index": 4,
                        },
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 614,
                    "next_leg_index": 5,
                    "original_location": ["42.2657459", "-71.6197564"],
                    "prev_leg_index": 4,
                    "location": ["42.265746", "-71.619756"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 614,
                            "job_index": 2,
                            "job_id": "1636833644da62f4f8",
                            "index": 7,
                            "type": "job",
                            "waypoint_index": 5,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 731,
                    "next_leg_index": 6,
                    "original_location": ["42.2661395", "-71.6196923"],
                    "prev_leg_index": 5,
                    "location": ["42.26614", "-71.619692"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 731,
                            "job_index": 0,
                            "job_id": "1636996904d664c081",
                            "index": 8,
                            "type": "job",
                            "waypoint_index": 6,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 841,
                    "next_leg_index": 7,
                    "original_location": ["42.2658711", "-71.6197059"],
                    "prev_leg_index": 6,
                    "location": ["42.265871", "-71.619706"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 841,
                            "job_index": 1,
                            "job_id": "162696835647e02ca3",
                            "index": 9,
                            "type": "job",
                            "waypoint_index": 7,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 940,
                    "next_leg_index": 8,
                    "original_location": ["42.2652214", "-71.6213596"],
                    "prev_leg_index": 7,
                    "location": ["42.265221", "-71.62136"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 940,
                            "job_index": 3,
                            "job_id": "16269764187a59999a",
                            "index": 10,
                            "type": "job",
                            "waypoint_index": 8,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1014,
                    "next_leg_index": 9,
                    "original_location": ["42.2641747", "-71.6234085"],
                    "prev_leg_index": 8,
                    "location": ["42.264175", "-71.623408"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1014,
                            "job_index": 4,
                            "job_id": "163671081394dd884b",
                            "index": 11,
                            "type": "job",
                            "waypoint_index": 9,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1109,
                    "next_leg_index": 10,
                    "original_location": ["42.262882", "-71.6236773"],
                    "prev_leg_index": 9,
                    "location": ["42.262882", "-71.623677"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1109,
                            "job_index": 5,
                            "job_id": "16276668627c77624d",
                            "index": 12,
                            "type": "job",
                            "waypoint_index": 10,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1197,
                    "next_leg_index": 11,
                    "original_location": ["42.2611384", "-71.6236325"],
                    "prev_leg_index": 10,
                    "location": ["42.261138", "-71.623632"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1197,
                            "job_index": 6,
                            "job_id": "163699703355f821d1",
                            "index": 13,
                            "type": "job",
                            "waypoint_index": 11,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1343,
                    "next_leg_index": 12,
                    "original_location": ["42.2570279", "-71.6223784"],
                    "prev_leg_index": 11,
                    "location": ["42.257028", "-71.622378"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1343,
                            "job_index": 7,
                            "job_id": "1631913595f9e25fbd",
                            "index": 14,
                            "type": "job",
                            "waypoint_index": 12,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1544,
                    "next_leg_index": 13,
                    "original_location": ["42.2547935", "-71.6222082"],
                    "prev_leg_index": 12,
                    "location": ["42.254793", "-71.622208"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1544,
                            "job_index": 8,
                            "job_id": "1639767148cb2b631f",
                            "index": 15,
                            "type": "job",
                            "waypoint_index": 13,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1874,
                    "next_leg_index": 14,
                    "original_location": ["42.2575424", "-71.6075095"],
                    "prev_leg_index": 13,
                    "location": ["42.257542", "-71.60751"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1874,
                            "job_index": 16,
                            "job_id": "16287945166521bf68",
                            "index": 16,
                            "type": "job",
                            "waypoint_index": 14,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2009,
                    "next_leg_index": 15,
                    "original_location": ["42.2610011", "-71.6113386"],
                    "prev_leg_index": 14,
                    "location": ["42.261001", "-71.611339"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2009,
                            "job_index": 15,
                            "job_id": "163683377016f52f6a",
                            "index": 17,
                            "type": "job",
                            "waypoint_index": 15,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2143,
                    "next_leg_index": 16,
                    "original_location": ["42.2637794", "-71.6122581"],
                    "prev_leg_index": 15,
                    "location": ["42.263779", "-71.612258"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2143,
                            "job_index": 13,
                            "job_id": "1639043323f9d753a6",
                            "index": 18,
                            "type": "job",
                            "waypoint_index": 16,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2222,
                    "next_leg_index": 17,
                    "original_location": ["42.2638349", "-71.6139788"],
                    "prev_leg_index": 16,
                    "location": ["42.263835", "-71.613979"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2222,
                            "job_index": 12,
                            "job_id": "16390031301c181540",
                            "index": 19,
                            "type": "job",
                            "waypoint_index": 17,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2297,
                    "next_leg_index": 18,
                    "original_location": ["42.2625776", "-71.6134729"],
                    "prev_leg_index": 17,
                    "location": ["42.262578", "-71.613473"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2297,
                            "job_index": 14,
                            "job_id": "1631303033989b471a",
                            "index": 20,
                            "type": "job",
                            "waypoint_index": 18,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2383,
                    "next_leg_index": 19,
                    "original_location": ["42.264034", "-71.6145734"],
                    "prev_leg_index": 18,
                    "location": ["42.264034", "-71.614573"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2383,
                            "job_index": 11,
                            "job_id": "163725764799196a3b",
                            "index": 21,
                            "type": "job",
                            "waypoint_index": 19,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2449,
                    "next_leg_index": 20,
                    "original_location": ["42.2638895", "-71.6148601"],
                    "prev_leg_index": 19,
                    "location": ["42.263889", "-71.61486"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2449,
                            "job_index": 9,
                            "job_id": "163491313739a59424",
                            "index": 22,
                            "type": "job",
                            "waypoint_index": 20,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2512,
                    "next_leg_index": 21,
                    "original_location": ["42.2641413", "-71.6150307"],
                    "prev_leg_index": 20,
                    "location": ["42.264141", "-71.615031"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2512,
                            "job_index": 10,
                            "job_id": "162878819891c90967",
                            "index": 23,
                            "type": "job",
                            "waypoint_index": 21,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2628,
                    "next_leg_index": 22,
                    "original_location": ["42.2681414", "-71.6165041"],
                    "prev_leg_index": 21,
                    "location": ["42.268141", "-71.616504"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2628,
                            "job_index": 20,
                            "job_id": "16269726019612e23c",
                            "index": 24,
                            "type": "job",
                            "waypoint_index": 22,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2712,
                    "next_leg_index": 23,
                    "original_location": ["42.2700426", "-71.6197787"],
                    "prev_leg_index": 22,
                    "location": ["42.270043", "-71.619779"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2712,
                            "job_index": 23,
                            "job_id": "1631045682a037253e",
                            "index": 25,
                            "type": "job",
                            "waypoint_index": 23,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 2799,
                    "next_leg_index": 24,
                    "original_location": ["42.2700918", "-71.621203"],
                    "prev_leg_index": 23,
                    "location": ["42.270092", "-71.621203"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 2799,
                            "job_index": 25,
                            "job_id": "1626976534677118e5",
                            "index": 26,
                            "type": "job",
                            "waypoint_index": 24,
                        }
                    ],
                },
                {
                    "duration": 0,
                    "start_time": 2889,
                    "original_location": ["42.270017", "-71.623672"],
                    "location": ["42.270017", "-71.623672"],
                    "prev_leg_index": 24,
                    "actions": [
                        {
                            "duration": 0,
                            "index": 27,
                            "start_time": 2889,
                            "type": "end",
                            "waypoint_index": 25,
                        }
                    ],
                },
            ],
        },
        {
            "driver_name": "Ricky Joseph",
            "start_time": 0,
            "driver_id": "61de279b-24d0-4b7e-bd5d-497f9b9ffd90",
            "agent_id": "1640635614944a7939",
            "distance": 8878,
            "school_id": "BOS2",
            "end_time": 2042,
            "time": 2042,
            "preferred_time_info": {
                "time_range_pm": {
                    "end_time": "05:00:00",
                    "time_window": 7200,
                    "start_time": "03:00:00",
                },
                "time_range_am": {
                    "end_time": "09:00:00",
                    "time_window": 10800,
                    "start_time": "06:00:00",
                },
            },
            "waypoints": [
                {
                    "duration": 0,
                    "start_time": 0,
                    "next_leg_index": 0,
                    "original_location": ["42.270017", "-71.623672"],
                    "location": ["42.270017", "-71.623672"],
                    "actions": [
                        {
                            "duration": 0,
                            "index": 0,
                            "start_time": 0,
                            "type": "start",
                            "waypoint_index": 0,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 68,
                    "next_leg_index": 1,
                    "original_location": ["42.27296834231933", "-71.62923427181497"],
                    "prev_leg_index": 0,
                    "location": ["42.272968", "-71.629234"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 68,
                            "job_index": 26,
                            "job_id": "16369968431bf055ca",
                            "index": 1,
                            "type": "job",
                            "waypoint_index": 1,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 175,
                    "next_leg_index": 2,
                    "original_location": ["42.27094879831655", "-71.6315621587745"],
                    "prev_leg_index": 1,
                    "location": ["42.270949", "-71.631562"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 175,
                            "job_index": 28,
                            "job_id": "1622648858cb9fa2eb",
                            "index": 2,
                            "type": "job",
                            "waypoint_index": 2,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 255,
                    "next_leg_index": 3,
                    "original_location": ["42.27134232698006", "-71.63494526576292"],
                    "prev_leg_index": 2,
                    "location": ["42.271342", "-71.634945"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 255,
                            "job_index": 29,
                            "job_id": "16353631019c9808c7",
                            "index": 3,
                            "type": "job",
                            "waypoint_index": 3,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 325,
                    "next_leg_index": 4,
                    "original_location": ["42.27175515316891", "-71.63441955282066"],
                    "prev_leg_index": 3,
                    "location": ["42.271755", "-71.63442"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 325,
                            "job_index": 30,
                            "job_id": "16269762790928cd9b",
                            "index": 4,
                            "type": "job",
                            "waypoint_index": 4,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 434,
                    "next_leg_index": 5,
                    "original_location": ["42.27439876450747", "-71.63035332416642"],
                    "prev_leg_index": 4,
                    "location": ["42.274399", "-71.630353"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 434,
                            "job_index": 31,
                            "job_id": "16385275479c4db01c",
                            "index": 5,
                            "type": "job",
                            "waypoint_index": 5,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 531,
                    "next_leg_index": 6,
                    "original_location": ["42.27551015957372", "-71.626662604735"],
                    "prev_leg_index": 5,
                    "location": ["42.27551", "-71.626663"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 531,
                            "job_index": 32,
                            "job_id": "1626888290a3f9e775",
                            "index": 6,
                            "type": "job",
                            "waypoint_index": 6,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 641,
                    "next_leg_index": 7,
                    "original_location": ["42.27523231269541", "-71.62310063089105"],
                    "prev_leg_index": 6,
                    "location": ["42.275232", "-71.623101"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 641,
                            "job_index": 42,
                            "job_id": "1626977265b0f6c001",
                            "index": 7,
                            "type": "job",
                            "waypoint_index": 7,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 748,
                    "next_leg_index": 8,
                    "original_location": ["42.276970820500814", "-71.62539660211117"],
                    "prev_leg_index": 7,
                    "location": ["42.276971", "-71.625397"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 748,
                            "job_index": 37,
                            "job_id": "16287940094a8e2119",
                            "index": 8,
                            "type": "job",
                            "waypoint_index": 8,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 925,
                    "next_leg_index": 9,
                    "original_location": ["42.278518766526716", "-71.62114798285201"],
                    "prev_leg_index": 8,
                    "location": ["42.278519", "-71.621148"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 925,
                            "job_index": 40,
                            "job_id": "163977819309414de7",
                            "index": 9,
                            "type": "job",
                            "waypoint_index": 9,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 996,
                    "next_leg_index": 10,
                    "original_location": ["42.27823299473865", "-71.62005364159859"],
                    "prev_leg_index": 9,
                    "location": ["42.278233", "-71.620054"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 996,
                            "job_index": 41,
                            "job_id": "1639753254bf86e370",
                            "index": 10,
                            "type": "job",
                            "waypoint_index": 10,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1087,
                    "next_leg_index": 11,
                    "original_location": ["42.27681205463209", "-71.62263929096211"],
                    "prev_leg_index": 10,
                    "location": ["42.276812", "-71.622639"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1087,
                            "job_index": 43,
                            "job_id": "1631111040787a951a",
                            "index": 11,
                            "type": "job",
                            "waypoint_index": 11,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1181,
                    "next_leg_index": 12,
                    "original_location": ["42.27784402549247", "-71.626029603409"],
                    "prev_leg_index": 11,
                    "location": ["42.277844", "-71.62603"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1181,
                            "job_index": 36,
                            "job_id": "1631912627580891d0",
                            "index": 12,
                            "type": "job",
                            "waypoint_index": 12,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1317,
                    "next_leg_index": 13,
                    "original_location": ["42.27930463227037", "-71.62555753462087"],
                    "prev_leg_index": 12,
                    "location": ["42.279305", "-71.625558"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1317,
                            "job_index": 38,
                            "job_id": "162697713657f77819",
                            "index": 13,
                            "type": "job",
                            "waypoint_index": 13,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1421,
                    "next_leg_index": 14,
                    "original_location": ["42.28145579037091", "-71.62646948563311"],
                    "prev_leg_index": 13,
                    "location": ["42.281456", "-71.626469"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1421,
                            "job_index": 39,
                            "job_id": "16379540582e6a6f6b",
                            "index": 14,
                            "type": "job",
                            "waypoint_index": 14,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1569,
                    "next_leg_index": 15,
                    "original_location": ["42.27946339181345", "-71.6313725635161"],
                    "prev_leg_index": 14,
                    "location": ["42.279463", "-71.631373"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1569,
                            "job_index": 35,
                            "job_id": "16287915812b11b8b5",
                            "index": 15,
                            "type": "job",
                            "waypoint_index": 15,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1667,
                    "next_leg_index": 16,
                    "original_location": ["42.27775670551492", "-71.62994562839162"],
                    "prev_leg_index": 15,
                    "location": ["42.277757", "-71.629946"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1667,
                            "job_index": 34,
                            "job_id": "16288773545141c088",
                            "index": 16,
                            "type": "job",
                            "waypoint_index": 16,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1773,
                    "next_leg_index": 17,
                    "original_location": ["42.27783608729687", "-71.62796079381368"],
                    "prev_leg_index": 16,
                    "location": ["42.277836", "-71.627961"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1773,
                            "job_index": 33,
                            "job_id": "16390452027af06539",
                            "index": 17,
                            "type": "job",
                            "waypoint_index": 17,
                        }
                    ],
                },
                {
                    "duration": 60,
                    "start_time": 1898,
                    "next_leg_index": 18,
                    "original_location": ["42.27320199128101", "-71.62583303837653"],
                    "prev_leg_index": 17,
                    "location": ["42.273202", "-71.625833"],
                    "actions": [
                        {
                            "duration": 60,
                            "start_time": 1898,
                            "job_index": 27,
                            "job_id": "1628794721590a3ea1",
                            "index": 18,
                            "type": "job",
                            "waypoint_index": 18,
                        }
                    ],
                },
                {
                    "duration": 0,
                    "start_time": 2042,
                    "original_location": ["42.270017", "-71.623672"],
                    "location": ["42.270017", "-71.623672"],
                    "prev_leg_index": 18,
                    "actions": [
                        {
                            "duration": 0,
                            "index": 19,
                            "start_time": 2042,
                            "type": "end",
                            "waypoint_index": 19,
                        }
                    ],
                },
            ],
        },
    ],
}


def optimise_route(planned_routes):
    for route in planned_routes["request_file_path"]:
        optimized_waypoints = []
        i = 1
        optimized_waypoints.append(route["waypoints"][0])
        while i < len(route["waypoints"]) - 2:
            if route["waypoints"][i + 1]["start_time"] - route["waypoints"][i]["start_time"] < 110:
                temp = {
                    "duration": route["waypoints"][i]["duration"],
                    "start_time": route["waypoints"][i]["start_time"],
                    "original_location": route["waypoints"][i]["original_location"],
                    "location": route["waypoints"][i]["location"],
                    "actions": route["waypoints"][i]["actions"]
                    + route["waypoints"][i + 1]["actions"],
                }
                optimized_waypoints.append(temp)
                i += 2
            else:
                optimized_waypoints.append(route["waypoints"][i])
                i += 1
        optimized_waypoints.append(route["waypoints"][-1])

        for j in range(len(optimized_waypoints)):
            if j == 0:
                optimized_waypoints[j]["next_leg_index"] = 0
            elif j == len(optimized_waypoints) - 1:
                optimized_waypoints[j]["prev_leg_index"] = j - 1
            else:
                optimized_waypoints[j]["next_leg_index"] = j
                optimized_waypoints[j]["prev_leg_index"] = j - 1

            for k in range(len(optimized_waypoints[j]["actions"])):
                optimized_waypoints[j]["actions"][k]["waypoint_index"] = j

        route["waypoints"] = optimized_waypoints


def time_difference(planned_routes):
    for waypoint in range(len(planned_routes["request_file_path"][0]["waypoints"]) - 1):
        print(
            planned_routes["request_file_path"][0]["waypoints"][waypoint + 1]["start_time"]
            - planned_routes["request_file_path"][0]["waypoints"][waypoint]["start_time"]
        )


def get_lat_lng(planned_routes):
    geo = []
    for waypoint in planned_routes["request_file_path"][0]["waypoints"]:
        geo.append(waypoint["original_location"])

    return geo


# temp_route = route.copy()
# print(json.dumps(get_lat_lng(temp_route), indent=2))
# print(len(temp_route["request_file_path"][1]["waypoints"]))
# optimise_route(temp_route)
# print(json.dumps(temp_route, indent=2))

[
    ["42.270017", "-71.623672"],
    ["42.2705644", "-71.6212994"],
    ["42.2703619", "-71.617174"],
    ["42.2697458", "-71.6152395"],
    ["42.2681683", "-71.6163167"],
    ["42.2657459", "-71.6197564"],
    ["42.2661395", "-71.6196923"],
    ["42.2658711", "-71.6197059"],
    ["42.2652214", "-71.6213596"],
    ["42.2641747", "-71.6234085"],
    ["42.262882", "-71.6236773"],
    ["42.2611384", "-71.6236325"],
    ["42.2570279", "-71.6223784"],
    ["42.2547935", "-71.6222082"],
    ["42.2575424", "-71.6075095"],
    ["42.2610011", "-71.6113386"],
    ["42.2637794", "-71.6122581"],
    ["42.2638349", "-71.6139788"],
    ["42.2625776", "-71.6134729"],
    ["42.264034", "-71.6145734"],
    ["42.2638895", "-71.6148601"],
    ["42.2641413", "-71.6150307"],
    ["42.2681414", "-71.6165041"],
    ["42.2700426", "-71.6197787"],
    ["42.2700918", "-71.621203"],
    ["42.270017", "-71.623672"],
]

[
    [42.270009724690716, -71.62366636334244],
    [42.27069932215604, -71.62147611429168],
    [42.270525500000005, -71.61744300000001],
    [42.26971123135388, -71.61521058438197],
    [42.2679591, -71.61610259999999],
    [42.26601588311179, -71.61916803313596],
    [42.26628226295054, -71.61940285500384],
    [42.26608957632945, -71.61922977978715],
    [42.26477696973278, -71.62122631410311],
    [42.2639199898196, -71.62315863031498],
    [42.262869, -71.62392],
    [42.26129233588797, -71.62329174937221],
    [42.257492607447865, -71.607576708405],
    [42.26414454008677, -71.61235029548337],
    [42.26384240092566, -71.61377620819412],
    [42.26254465869948, -71.61368674775869],
    [42.26400959706818, -71.614546474999],
    [42.26389746462641, -71.6148450214511],
    [42.264123982036864, -71.61506348615588],
    [42.26792631846174, -71.61680014608791],
    [42.270093313141004, -71.61971432903846],
    [42.2698742, -71.6214303],
    [42.270009724690716, -71.62366636334244],
]
