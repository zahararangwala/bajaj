import requests 

your_name = "Zahara Rangwala"
your_reg_no = "0827AL221156"
your_email = "zahararangwala@gmail.com"

user_info = {
    "name": your_name,
    "regNo": your_reg_no,
    "email": your_email
}

print("Generating webhook...")

response = requests.post(
    "https://bfhldevapigw.healthrx.co.in/hiring/generateWebhook/PYTHON",
    json=user_info
)


if response.status_code == 200:
    result = response.json()
    webhook_url = result.get("webhook")
    access_token = result.get("accessToken")

    print("Webhook URL received:", webhook_url)
    print("Access Token received:", access_token)
else:
    print("Failed to generate webhook. Status code:", response.status_code)
    print(response.text)
    exit()

last_digit = int(your_reg_no[-1])

if last_digit % 2 == 1:
    print("\nYou need to solve SQL QUESTION 1:")
    print("https://drive.google.com/file/d/1q8F8g0EpyNzd5BWk-voe5CKbsxoskJWY/view?usp=sharing")
else:
    print("\nYou need to solve SQL QUESTION 2:")
    print("https://drive.google.com/file/d/1_PO_1ZvmDqAZJv77XRYsVben11Wp2HVb/view?usp=sharing")

final_sql_query = """
SELECT 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME,
    COUNT(e2.EMP_ID) AS YOUNGER_EMPLOYEES_COUNT
FROM EMPLOYEE e1
JOIN DEPARTMENT d ON e1.DEPARTMENT = d.DEPARTMENT_ID
LEFT JOIN EMPLOYEE e2 
    ON e1.DEPARTMENT = e2.DEPARTMENT 
    AND e2.DOB > e1.DOB
GROUP BY 
    e1.EMP_ID,
    e1.FIRST_NAME,
    e1.LAST_NAME,
    d.DEPARTMENT_NAME
ORDER BY e1.EMP_ID DESC;
"""

headers = {
    "Authorization": access_token,
    "Content-Type": "application/json"
}

submission_data = {
    "finalQuery": final_sql_query.strip()
}

print("\nSubmitting your SQL query...")

submit_response = requests.post(
    webhook_url,
    headers=headers,
    json=submission_data
)


print("Webhook response status code:", submit_response.status_code)
print("Response text:", submit_response.text)

if submit_response.status_code == 200:
    print(" SQL query submitted successfully!")
else:
    print(" Submission failed.")
    print("Status code:", submit_response.status_code)
    print(submit_response.text)
