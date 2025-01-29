import json

households_people = json.loads(r'''
{
    "links": {
        "self": "https://api.planningcenteronline.com/people/v2/households/6759685/people?include=field_data"
    },
    "data": [
        {
            "type": "Person",
            "id": "36729400",
            "attributes": {
                "accounting_administrator": true,
                "anniversary": "2000-08-12",
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg",
                "birthdate": "1975-11-20",
                "can_create_forms": true,
                "can_email_lists": true,
                "child": false,
                "created_at": "2018-04-25T19:15:47Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg",
                "directory_status": "participant",
                "first_name": "Rob",
                "gender": "Male",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "login_identifier": "rob@cbclilburn.org",
                "medical_notes": "Testing a form",
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Rob Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": "Manager",
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": true
                },
                "school_type": null,
                "site_administrator": true,
                "status": "active",
                "updated_at": "2024-10-30T20:33:53Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951685"
                    }
                },
                "field_data": {
                    "links": {
                        "related": "https://api.planningcenteronline.com/people/v2/people/36729400/field_data"
                    },
                    "data": [
                        {
                            "type": "FieldDatum",
                            "id": "79152227"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "79152514"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "83246442"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "93603536"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "97200340"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "105500517"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "106206416"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "106206430"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992160"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992161"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992162"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992163"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "173239287"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "202515041"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "212172641"
                        }
                    ]
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/36729400",
                "html": "https://people.planningcenteronline.com/people/AC36729400"
            }
        },
        {
            "type": "Person",
            "id": "49166778",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": "2000-08-12",
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg",
                "birthdate": "1978-03-05",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2019-02-28T23:49:27Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg",
                "directory_status": "no_access",
                "first_name": "Tammy",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "login_identifier": "tskocher@gmail.com",
                "medical_notes": null,
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Tammy Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": "Viewer",
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": true
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2023-09-05T21:02:23Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                },
                "field_data": {
                    "links": {
                        "related": "https://api.planningcenteronline.com/people/v2/people/49166778/field_data"
                    },
                    "data": [
                        {
                            "type": "FieldDatum",
                            "id": "44390872"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "44390876"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "44390880"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "44390882"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "79152324"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "79152615"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "83246444"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "93603537"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "97072483"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "104928265"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "105500619"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "173239292"
                        }
                    ]
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/49166778",
                "html": "https://people.planningcenteronline.com/people/AC49166778"
            }
        },
        {
            "type": "Person",
            "id": "49657796",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": null,
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png",
                "birthdate": "2003-11-16",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2019-03-06T21:24:37Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png",
                "directory_status": "no_access",
                "first_name": "Charisa",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "login_identifier": "horseback89@gmail.com",
                "medical_notes": null,
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Charisa Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": null,
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": false
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2023-09-05T21:01:45Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                },
                "field_data": {
                    "links": {
                        "related": "https://api.planningcenteronline.com/people/v2/people/49657796/field_data"
                    },
                    "data": [
                        {
                            "type": "FieldDatum",
                            "id": "94239980"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "94239981"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "105500816"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "149698030"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "149698031"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "173239231"
                        }
                    ]
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/49657796",
                "html": "https://people.planningcenteronline.com/people/AC49657796"
            }
        },
        {
            "type": "Person",
            "id": "76460632",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": null,
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png",
                "birthdate": "2008-09-25",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2020-05-12T20:47:33Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png",
                "directory_status": "no_access",
                "first_name": "Kupo",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "login_identifier": "kupokocherpup@gmail.com",
                "medical_notes": null,
                "membership": "Friend of CBC",
                "middle_name": null,
                "name": "Kupo Kocher",
                "nickname": null,
                "passed_background_check": false,
                "people_permissions": null,
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": false
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2024-08-20T13:43:39Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": {
                        "type": "PrimaryCampus",
                        "id": "38718"
                    }
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                },
                "field_data": {
                    "links": {
                        "related": "https://api.planningcenteronline.com/people/v2/people/76460632/field_data"
                    },
                    "data": [
                        {
                            "type": "FieldDatum",
                            "id": "93863255"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "93863256"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "93863257"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "105500923"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "114330824"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "114330825"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "114342416"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "114342705"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "124120641"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992713"
                        },
                        {
                            "type": "FieldDatum",
                            "id": "145992714"
                        }
                    ]
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/76460632",
                "html": "https://people.planningcenteronline.com/people/AC76460632"
            }
        }
    ],
    "included": [
        {
            "type": "FieldDatum",
            "id": "79152227",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372456"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/79152227"
            }
        },
        {
            "type": "FieldDatum",
            "id": "79152514",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372455"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/79152514"
            }
        },
        {
            "type": "FieldDatum",
            "id": "83246442",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "10/31/2010"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372454"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/83246442"
            }
        },
        {
            "type": "FieldDatum",
            "id": "93603536",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Fall 2010 (Bryan Taylor)"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "379413"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/93603536"
            }
        },
        {
            "type": "FieldDatum",
            "id": "97200340",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-36729400/field-definition-379414-5d4fe0c6ee88d5a3a803/Rob_Kocher.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=1d047c1cc6c512d3bcf1cd2a5023a899c946ec31560693ebde9f3f29d8f746cc"
                },
                "file_content_type": "application/pdf",
                "file_name": "Rob_Kocher.pdf",
                "file_size": 62734,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "379414"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/97200340"
            }
        },
        {
            "type": "FieldDatum",
            "id": "105500517",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457479"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/105500517"
            }
        },
        {
            "type": "FieldDatum",
            "id": "106206416",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-36729400/field-definition-457480-07a2f781b1cca88b7d6e/SOF-Rob_Kocher.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=7278e66088cc996e680bae054b49f23552c08d663c193dc6b18b88a593bd7072"
                },
                "file_content_type": "application/pdf",
                "file_name": "SOF-Rob_Kocher.pdf",
                "file_size": 130466,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457480"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/106206416"
            }
        },
        {
            "type": "FieldDatum",
            "id": "106206430",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "09/05/2024"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "253130"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/106206430"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992160",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "09/29/2022"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587885"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992160"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992161",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "09/29/2022"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587887"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992161"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992162",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-36729400/field-definition-587886-cb50a1372df791166906/Kocher__Rob_Child_Protection_Policy_TEST.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=448c6685bb4aec9db43e846a435a36d5fdc10bedf4302c87bde29f46174f0bd7"
                },
                "file_content_type": "application/pdf",
                "file_name": "Kocher__Rob_Child_Protection_Policy_TEST.pdf",
                "file_size": 16657,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587886"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992162"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992163",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-36729400/field-definition-587888-1dde1a89c771ec1c3e2a/Kocher__Rob_Background_Check_TEST.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=06fd93f6e21393374419fd3e275518cf2b8e87a239cc5f16e08e612bbe42edce"
                },
                "file_content_type": "application/pdf",
                "file_name": "Kocher__Rob_Background_Check_TEST.pdf",
                "file_size": 15996,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587888"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992163"
            }
        },
        {
            "type": "FieldDatum",
            "id": "173239287",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Use"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "684983"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/173239287"
            }
        },
        {
            "type": "FieldDatum",
            "id": "202515041",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Prayer"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "421715"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/202515041"
            }
        },
        {
            "type": "FieldDatum",
            "id": "212172641",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "830513"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/212172641"
            }
        },
        {
            "type": "FieldDatum",
            "id": "44390872",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Missionary"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "253126"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/44390872"
            }
        },
        {
            "type": "FieldDatum",
            "id": "44390876",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "252621"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/44390876"
            }
        },
        {
            "type": "FieldDatum",
            "id": "44390880",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "253192"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/44390880"
            }
        },
        {
            "type": "FieldDatum",
            "id": "44390882",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Evangelical Free, Bible Church, and Baptist"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "257599"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/44390882"
            }
        },
        {
            "type": "FieldDatum",
            "id": "79152324",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372456"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/79152324"
            }
        },
        {
            "type": "FieldDatum",
            "id": "79152615",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372455"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/79152615"
            }
        },
        {
            "type": "FieldDatum",
            "id": "83246444",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "10/31/2010"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372454"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/83246444"
            }
        },
        {
            "type": "FieldDatum",
            "id": "93603537",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Fall 2010 (Bryan Taylor)"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "379413"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/93603537"
            }
        },
        {
            "type": "FieldDatum",
            "id": "97072483",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-49166778/field-definition-379414-801d28b58cf0464a4cbe/Tammy_Kocher.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=eefb763f3f589fb583b706956a73a8bef4d252b3d5bfc47bafd2449f92dd2490"
                },
                "file_content_type": "application/pdf",
                "file_name": "Tammy_Kocher.pdf",
                "file_size": 57165,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "379414"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/97072483"
            }
        },
        {
            "type": "FieldDatum",
            "id": "104928265",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Tammy's Grandmother, Anita, passed away 4/23/21\r\nTammy's Grandma, Grandma Stark, passed away on 5/5/21"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "421712"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/104928265"
            }
        },
        {
            "type": "FieldDatum",
            "id": "105500619",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457479"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/105500619"
            }
        },
        {
            "type": "FieldDatum",
            "id": "173239292",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Use"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "684983"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49166778"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/173239292"
            }
        },
        {
            "type": "FieldDatum",
            "id": "94239980",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372455"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/94239980"
            }
        },
        {
            "type": "FieldDatum",
            "id": "94239981",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372456"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/94239981"
            }
        },
        {
            "type": "FieldDatum",
            "id": "105500816",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "true"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457479"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/105500816"
            }
        },
        {
            "type": "FieldDatum",
            "id": "149698030",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "10/30/2022"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "253130"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/149698030"
            }
        },
        {
            "type": "FieldDatum",
            "id": "149698031",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-49657796/field-definition-457480-a80351ab43e5f730d3c9/Charisa_Kocher.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=5c9d2cc83e2fd3bc7c9a688ae65ce8f07d71eb68ff0ea387685cee5d934b3fca"
                },
                "file_content_type": "application/pdf",
                "file_name": "Charisa_Kocher.pdf",
                "file_size": 124575,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457480"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/149698031"
            }
        },
        {
            "type": "FieldDatum",
            "id": "173239231",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Use"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "684983"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "49657796"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/173239231"
            }
        },
        {
            "type": "FieldDatum",
            "id": "93863255",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372455"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/93863255"
            }
        },
        {
            "type": "FieldDatum",
            "id": "93863256",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "372456"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/93863256"
            }
        },
        {
            "type": "FieldDatum",
            "id": "93863257",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Furry Friends cannot sign with paws."
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "379412"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/93863257"
            }
        },
        {
            "type": "FieldDatum",
            "id": "105500923",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "false"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "457479"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/105500923"
            }
        },
        {
            "type": "FieldDatum",
            "id": "114330824",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Do Not Track Birthdays"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "421714"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/114330824"
            }
        },
        {
            "type": "FieldDatum",
            "id": "114330825",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Testing Do Not Track Birthdays"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "421715"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/114330825"
            }
        },
        {
            "type": "FieldDatum",
            "id": "114342416",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "Do Not Put In Printed Directory"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "483637"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/114342416"
            }
        },
        {
            "type": "FieldDatum",
            "id": "114342705",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "If we add Kupo to the printed directory, we'll need to start adding every other dog in the church family.  While a worthy thing to do, we should ideally get the humans sorted out first.  Perhaps a separate directory can be created for dog lovers. ;)"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "483640"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/114342705"
            }
        },
        {
            "type": "FieldDatum",
            "id": "124120641",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "The first time Kupo came to church, she was scared to death.  She shook like a leaf.  Now, she bounds on her way in!"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "517584"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/124120641"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992713",
            "attributes": {
                "file": {
                    "url": null
                },
                "file_content_type": null,
                "file_name": null,
                "file_size": null,
                "value": "09/29/2022"
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587887"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992713"
            }
        },
        {
            "type": "FieldDatum",
            "id": "145992714",
            "attributes": {
                "file": {
                    "url": "https://account-center-production.s3.amazonaws.com/uploads/field_datum/organization-255841/person-76460632/field-definition-587888-324e20b16f56ad0e7060/Kupo_Background_Check.pdf?X-Amz-Expires=600&X-Amz-Date=20241110T133742Z&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLWVhc3QtMSJIMEYCIQC0nkpgZbMyQJ6523%2FeBVfwsSWEYaPnYAqDhlwA7D7OXgIhAKShhQ13LRVlo%2Bb%2Bh7pnpLoDwvdKT8aJqsfVbLJA%2BPo1KoQECIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQBBoMNTY5MzA3MzI4MjE5IgxwJT9uVFdWnpaelHoq2AMwbOolUvb9HFQkquSg002wq7lse0XstlZTxAmCC4HWl%2BMq2oftHaEj2BfAMrxZ8vLKfMqeoeJ4bxEvKVCX3xQBsL7DV74eaKl%2F4yCu2vapoDAqQejhhDVlaxjKq%2BwZq3V%2Fj1SMywWzYjy90qyFvxIi6ejkIhEVRudYZQ4N5o9LNd2rSoImptbzxNSDq70cPqh0uWXycJ43DRHxO4KEt46rbEU19UZLO0MATl1i6KMISL1QBB6whuKxI%2BCBQ9Fz2g2PirGzepbzMVN2AcwzTWwIt%2F4X0TDvzzhr6AI3vru5MEZsgCpyJW%2F70XLpSycUZfF2hJwXMZy9e578rf315BheKdDw30jj6uMDhFqTZUw2%2B5mKbboYSrxNXlA6plUghvrULVRn7PPH2hGCDrEsa7QvXfj4N0uwpRnKXsY9phgR462EgK%2FMOrVCvelOtosPFczl0N1EBXGeRmbLfLQ9teYUvU2QtYOP4NEuWJ5OjbmnfEsMoo4h3hM9OKMjDRK7lnKHdW9MlN5oqyrdbGoRkZ7vlPQORUQKKO02iOPUinNulXOZFzyqDOB2C2707c65FDkxV6R0XJcInSUBaWWhUYeOS2RF9rw9nAAfU8zboZONJoZZ68XOIgN6MJbuwbkGOqQBO5xIwqpUoFSjf8fGFAlBtqnyMO%2FNoQA5u4cek7tx2I%2FrUiSjEpnsUMm1B7320VsR84JxSan4iC15C4bLmfhMxHleXlqNA1ENaQml7Ft0TzNzyVEFn7Qx7NeYUmLn2INsv0%2Bm3NNdQ9GBLoigQQCO4%2F381DcCDZQqmUSX0e1QP%2FzVxQ8uOUk0EZQBvppVraco35Z%2FDNpDX8yi%2FTYzvWjy%2B9T7PR4%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAYJDK4N3N7VDO7ZWP%2F20241110%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=host&X-Amz-Signature=54059d7b7fbf7fb712a3c2dc7cc67152b5529f3169e267d0e98114bf234dc1ae"
                },
                "file_content_type": "application/pdf",
                "file_name": "Kupo_Background_Check.pdf",
                "file_size": 16261,
                "value": null
            },
            "relationships": {
                "field_definition": {
                    "data": {
                        "type": "FieldDefinition",
                        "id": "587888"
                    }
                },
                "customizable": {
                    "data": {
                        "type": "Person",
                        "id": "76460632"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/field_data/145992714"
            }
        }
    ],
    "meta": {
        "total_count": 4,
        "count": 4,
        "can_order_by": [
            "accounting_administrator",
            "anniversary",
            "birthdate",
            "child",
            "given_name",
            "grade",
            "graduation_year",
            "last_name",
            "middle_name",
            "nickname",
            "people_permissions",
            "site_administrator",
            "gender",
            "inactivated_at",
            "created_at",
            "updated_at",
            "first_name",
            "remote_id",
            "membership",
            "status"
        ],
        "can_query_by": [
            "accounting_administrator",
            "anniversary",
            "birthdate",
            "child",
            "given_name",
            "grade",
            "graduation_year",
            "last_name",
            "middle_name",
            "nickname",
            "people_permissions",
            "site_administrator",
            "gender",
            "inactivated_at",
            "medical_notes",
            "membership",
            "created_at",
            "updated_at",
            "search_name_or_email_or_phone_number",
            "search_name_or_email",
            "search_name",
            "search_phone_number_e164",
            "search_phone_number",
            "mfa_configured",
            "first_name",
            "id",
            "primary_campus_id",
            "remote_id",
            "status"
        ],
        "can_include": [
            "addresses",
            "emails",
            "field_data",
            "households",
            "inactive_reason",
            "marital_status",
            "name_prefix",
            "name_suffix",
            "organization",
            "person_apps",
            "phone_numbers",
            "platform_notifications",
            "primary_campus",
            "school",
            "social_profiles"
        ],
        "can_filter": [
            "without_deceased",
            "non_pending"
        ],
        "parent": {
            "id": "6759685",
            "type": "Household"
        }
    }
}
''')

single_household = json.loads(r'''
{
    "links": {
        "self": "https://api.planningcenteronline.com/people/v2/households?include=people&per_page=1",
        "next": "https://api.planningcenteronline.com/people/v2/households?include=people&offset=1&per_page=1"
    },
    "data": [
        {
            "type": "Household",
            "id": "6759685",
            "attributes": {
                "avatar": "https://avatars.planningcenteronline.com/uploads/household/6759685-1547489362/avatar.1.jpg",
                "created_at": "2019-01-14T18:09:22Z",
                "member_count": 4,
                "name": "Kocher Household",
                "primary_contact_id": "36729400",
                "primary_contact_name": "Rob Kocher",
                "updated_at": "2021-08-13T16:15:46Z"
            },
            "relationships": {
                "primary_contact": {
                    "data": {
                        "type": "Person",
                        "id": "36729400"
                    }
                },
                "people": {
                    "links": {
                        "related": "https://api.planningcenteronline.com/people/v2/households/6759685/people"
                    },
                    "data": [
                        {
                            "type": "Person",
                            "id": "36729400"
                        },
                        {
                            "type": "Person",
                            "id": "49166778"
                        },
                        {
                            "type": "Person",
                            "id": "49657796"
                        },
                        {
                            "type": "Person",
                            "id": "76460632"
                        }
                    ]
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/households/6759685"
            }
        }
    ],
    "included": [
        {
            "type": "Person",
            "id": "36729400",
            "attributes": {
                "accounting_administrator": true,
                "anniversary": "2000-08-12",
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg",
                "birthdate": "1975-11-20",
                "can_create_forms": true,
                "can_email_lists": true,
                "child": false,
                "created_at": "2018-04-25T19:15:47Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/36729400-1524683747/avatar.2.jpeg",
                "directory_status": "participant",
                "first_name": "Rob",
                "gender": "Male",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "medical_notes": "Testing a form",
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Rob Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": "Manager",
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": true
                },
                "school_type": null,
                "site_administrator": true,
                "status": "active",
                "updated_at": "2024-07-18T22:18:22Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951685"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/36729400",
                "html": "https://people.planningcenteronline.com/people/AC36729400"
            }
        },
        {
            "type": "Person",
            "id": "49166778",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": "2000-08-12",
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg",
                "birthdate": "1978-03-05",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2019-02-28T23:49:27Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/49166778-1551397767/avatar.2.jpg",
                "directory_status": "no_access",
                "first_name": "Tammy",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "medical_notes": null,
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Tammy Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": "Viewer",
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": true
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2023-09-05T21:02:23Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/49166778",
                "html": "https://people.planningcenteronline.com/people/AC49166778"
            }
        },
        {
            "type": "Person",
            "id": "49657796",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": null,
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png",
                "birthdate": "2003-11-16",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2019-03-06T21:24:37Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/49657796-1551907477/avatar.3.png",
                "directory_status": "no_access",
                "first_name": "Charisa",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "medical_notes": null,
                "membership": "Participant (CBC)",
                "middle_name": null,
                "name": "Charisa Kocher",
                "nickname": null,
                "passed_background_check": true,
                "people_permissions": null,
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": false
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2023-09-05T21:01:45Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": null
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/49657796",
                "html": "https://people.planningcenteronline.com/people/AC49657796"
            }
        },
        {
            "type": "Person",
            "id": "76460632",
            "attributes": {
                "accounting_administrator": false,
                "anniversary": null,
                "avatar": "https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png",
                "birthdate": "2008-09-25",
                "can_create_forms": false,
                "can_email_lists": false,
                "child": false,
                "created_at": "2020-05-12T20:47:33Z",
                "demographic_avatar_url": "https://avatars.planningcenteronline.com/uploads/person/76460632-1589316453/avatar.1.png",
                "directory_status": "no_access",
                "first_name": "Kupo",
                "gender": "Female",
                "given_name": null,
                "grade": null,
                "graduation_year": null,
                "inactivated_at": null,
                "last_name": "Kocher",
                "medical_notes": null,
                "membership": "Friend of CBC",
                "middle_name": null,
                "name": "Kupo Kocher",
                "nickname": null,
                "passed_background_check": false,
                "people_permissions": null,
                "remote_id": null,
                "resource_permission_flags": {
                    "can_access_workflows": false
                },
                "school_type": null,
                "site_administrator": false,
                "status": "active",
                "updated_at": "2024-08-20T13:43:39Z"
            },
            "relationships": {
                "primary_campus": {
                    "data": {
                        "type": "PrimaryCampus",
                        "id": "38718"
                    }
                },
                "gender": {
                    "data": {
                        "type": "Gender",
                        "id": "6951722"
                    }
                }
            },
            "links": {
                "self": "https://api.planningcenteronline.com/people/v2/people/76460632",
                "html": "https://people.planningcenteronline.com/people/AC76460632"
            }
        }
    ],
    "meta": {
        "total_count": 846,
        "count": 1,
        "next": {
            "offset": 1
        },
        "can_order_by": [
            "name",
            "member_count",
            "primary_contact_name",
            "created_at",
            "updated_at"
        ],
        "can_query_by": [
            "name",
            "member_count",
            "primary_contact_name",
            "created_at",
            "updated_at"
        ],
        "can_include": [
            "people"
        ],
        "parent": {
            "id": "255841",
            "type": "Organization"
        }
    }
}
''')
