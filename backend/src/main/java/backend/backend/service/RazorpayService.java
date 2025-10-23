package backend.backend.service;

import com.razorpay.*;
import org.json.JSONObject;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;

@Service
public class RazorpayService {


    private String keyId="rzp_test_RVPxvjAjcRvhXL";


    private String keySecret="QKwbfAzto7W4s4P4nZz4UkFi";

    public Order createOrder(int amountInRupees, String receiptId) throws RazorpayException {
        RazorpayClient client = new RazorpayClient(keyId, keySecret);

        JSONObject orderRequest = new JSONObject();
        orderRequest.put("amount", amountInRupees * 100); // amount in paise
        orderRequest.put("currency", "INR");
        orderRequest.put("receipt", receiptId);
        orderRequest.put("payment_capture", 1);

        return client.orders.create(orderRequest);
    }

    public boolean verifySignature(String orderId, String paymentId, String signature) {
        try {
            String payload = orderId + "|" + paymentId;
            return Utils.verifySignature(payload, signature, keySecret);
        } catch (Exception e) {
            return false;
        }
    }
}
