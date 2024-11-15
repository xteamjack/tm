{
    personal_info: {
        full_name:,
        name: {
            first,
            middle,
            last
        },
        date_of_birth,
        father_name,
        marital_status,
        gender,
        nationality,
    },
    identifiers: {
        aadhar,
        pan,
        passport: {
            number,
            issue_on,
            expires_on,
            issuing_authority,
            issued_at,
            issuing_country
        }
    }
    contact_info: {
        phone: {
            primary,
            alternative
        }
        email,
        address: {
            contact: {
                society,
                locality,
                landmark,
                city,
                state,
                country,
                pin
            }
        }
    },
    experience: [
        {
            organization,
            start_date: { month, year },
            end_date: { month, year },
            duration:{ years, months },
            designation,
        }
    ]
}