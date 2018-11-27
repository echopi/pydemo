from pywebpush import webpush, WebPushException

subscription_info = {"endpoint": "http://30.102.51.139:5010/wpush/m/1m2roo1wsCMlkxM3czkco49fMi88jwE5mTpYuPTlQFyTQQYlSPFc0BD6OSUTGy5e4_v1s8SsA7gwwObm_wlvpXAfcFOI68x06QCNySS0unL0CXuTftheA7FK7ObAH2Ei",
                     "keys": {"p256dh": "BAIikeAxnADcVUXvE3mrGROyqZUZwuih1rDMdO0Ws6Nm-uWjFdvmU1p3GDzBEyPDSMr7UD_zebUs98Ke7bQIbiY=", "auth": "AEP0LeUWXuQSwvsAuzYrHQ=="}}
vapid_private_key = 's2SMgiU-pOS-LcOXuONIXPWqgHbiBDUt4ulDsZOwQS0'
vapid_public_key = 'BJqNPfT8qNP-MnJXOnmWfU_bpekum0dA0Wt0hQxJOVb0Eg1cFRK0WgoUk9m2EoSCga-jRC3i_Hd2Ck0ljPgdeGk'

try:
  response = webpush(subscription_info,
                     data='{"notification":{"title":"Wow","body": "Happy!","click_action": "https://m.aliexpress.com","icon":"https://m.aliexpress.com/img/android-chrome-192x192.png"}}',
                     vapid_private_key=vapid_private_key,
                     vapid_claims={
                         "sub": "mailto:YourNameHere@example.org",
                     }
                     )
  print("push result: {} {}", response.ok, response.text)
except WebPushException as ex:
    print ex
    print("error: {}", repr(ex))
    # Mozilla returns additional information in the body of the response.
    print ex.response.text
    if ex.response and ex.response.json():
        extra = ex.response.json()
        print("Remote service replied with a {}:{}, {}",
              extra.code,
              extra.errno,
              extra.message
            )
