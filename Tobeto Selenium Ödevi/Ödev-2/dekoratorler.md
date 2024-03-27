```
@pytest.fixture: Bu decorator, fixture fonksiyonlarını parametreli hale getirir. Testlerde kullanılan veri veya kaynakları hazırlamak için kullanılır.
```
```
@pytest.mark.parametrize: Bu decorator, test fonksiyonlarına birden fazla argüman seti veya fixture’ı tanımlamak için kullanılır. Örneğin, farklı giriş değerleri için aynı test fonksiyonunu çalıştırmak istediğinizde kullanabilirsiniz.
```
```
@pytest.mark.skip: Bu decorator, belirli bir test fonksiyonunu her zaman atlamak için kullanılır. Örneğin, henüz tamamlanmamış veya geçici olarak devre dışı bırakılmış testleri işaretlemek için kullanılabilir.
```
```
@pytest.mark.skipif: Bu decorator, belirli bir koşulun sağlandığı durumlarda test fonksiyonunu atlamak için kullanılır. Örneğin, belirli bir işletim sistemi veya Python sürümü için testi atlamak istediğinizde kullanabilirsiniz.
```
```
@pytest.mark.usefixtures: Bu decorator, test fonksiyonlarına belirli bir fixture’ı otomatik olarak eklemek için kullanılır. Fixture’lar, testlerin çalışmasını sağlayan önemli bileşenlerdir.
```