import json

single_household = json.loads('''
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
