1. @pytest.fixture
```
Bu decorator, testlerde kullanılan bir fixture (araç) oluşturmak için kullanılır. Fixture’lar, testlerin çalışma ortamını hazırlamak, tekrar kullanılabilir test verileri sağlamak veya diğer hazırlık görevlerini gerçekleştirmek için kullanılır.
```

2. @pytest.mark.parametrize
```
Bu decorator, aynı test fonksiyonunu farklı parametrelerle birden fazla kez çağırmak için kullanılır. Bu, aynı mantığı farklı girişlerle test etmenin etkili bir yoludur.
```

3. @pytest.mark.skip ve @pytest.mark.skipif
```
Bu decorator’ler, belirli koşullar altında testleri atlamak için kullanılır. @pytest.mark.skip her zaman testi atlar, @pytest.mark.skipif ise belirli bir koşul sağlandığında testi atlar.
```
4. @pytest.mark.xfail
```
Bu decorator, testin bilerek başarısız olmasını beklediğimizi belirtmek için kullanılır. Yani, test hata vermese bile başarılı kabul edilmez.
```
5. @pytest.mark.usefixtures
```
Bu decorator, bir test fonksiyonu veya test sınıfının çalıştırılması için belirli fixture’ları kullanmayı sağlar. Fixture’lar, testlerin öncesi veya sonrası gibi belirli durumları hazırlamak veya temizlemek için kullanılan kaynaklardır.
```
6. @pytest.mark.timeout
```
Bu decorator, belirli bir test fonksiyonunun belirli bir süre içinde tamamlanmasını sağlar.
```
7. @pytest.fixture(autouse=True)
```
Bu decorator, bir fixture’ın test sınıfındaki her test fonksiyonu tarafından otomatik olarak kullanılmasını sağlar.
```

8. @pytest.yield_fixture
```
Bu decorator, bir fixture’ın test fonksiyonu tarafından kullanıldıktan sonra serbest bırakılmasını sağlar.
```

9. @pytest.raises
```
Bu decorator, belirli bir kodun belirli bir hatayı oluşturmasını sağlar.
```

10. @pytest.warns
```
Bu decorator, belirli bir kodun belirli bir uyarıyı oluşturmasını sağlar.
```

11. @pytest.deprecated
```
Bu decorator, belirli bir fonksiyonun veya özelliğin kullanımının eskimiş olduğunu gösterir.
```