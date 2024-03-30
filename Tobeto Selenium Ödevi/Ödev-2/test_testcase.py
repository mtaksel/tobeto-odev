from test_main import Test_Sauce


Test_Sauce().test_remove_from_card()
#Kullanıcı adı "standard_user" şifre "secret_sauce" ile login ol Sepete bir ürün ekle ve ürünü sepetten kaldır, sepette olmadığını kontrol et.

Test_Sauce().test_invalid_login()
# #pytest.mark.parametrize kullanarak geçersiz login yap.

Test_Sauce().test_empty_checkout_info()
# #Kullanıcı adı "standard_user" şifre "secret_sauce" ile login ol Sepete bir ürün ekle checkout infoya kadar ilerle ve "Error: First Name is required" hata mesajını goruntule

Test_Sauce().test_empty_login()
# #Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.

Test_Sauce().test_empty_pass_login()
#Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.

Test_Sauce().test_locked_out_user()
# #Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.

Test_Sauce().test_valid_login()
# #Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir. Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

Test_Sauce().test_add_to_cart()
# #Kullanıcı adı "standard_user" şifre "secret_sauce" ile login ol ve Sepete bir ürün ekle. ekledigin ürünün sepette olduğunu kontrol et.







