
# Описание датасета PhiUSIIL Phishing URL Dataset

Датасет PhiUSIIL содержит 134,850 легитимных и 100,945 фишинговых URL-адресов. 
Данные включают разнообразные признаки, извлеченные из исходного кода веб-страниц и самих URL. 
Эти признаки помогают различать фишинговые URL от легитимных.

---

## Описание столбцов

### Основная информация об URL
- **`FILENAME`**: Имя файла, содержащего URL.
- **`URL`**: Сам URL-адрес.
- **`URLLength`**: Длина URL.
- **`Domain`**: Доменное имя URL.
- **`DomainLength`**: Длина доменного имени.
- **`IsDomainIP`**: Флаг, указывающий, является ли домен IP-адресом (0 — нет, 1 — да).
- **`TLD`**: Доменная зона верхнего уровня (например, `.com`, `.org`).

### Параметры URL и домена
- **`URLSimilarityIndex`**: Индекс сходства URL с известными фишинговыми или легитимными URL.
- **`CharContinuationRate`**: Доля повторяющихся символов в URL.
- **`TLDLegitimateProb`**: Вероятность, что доменная зона принадлежит легитимному домену.
- **`URLCharProb`**: Вероятность появления символов URL.
- **`TLDLength`**: Длина доменной зоны.
- **`NoOfSubDomain`**: Количество поддоменов.

### Обфускация URL
- **`HasObfuscation`**: Флаг наличия обфускации в URL.
- **`NoOfObfuscatedChar`**: Количество обфусцированных символов.
- **`ObfuscationRatio`**: Доля обфусцированных символов.

### Статистика символов
- **`NoOfLettersInURL`**: Количество букв в URL.
- **`LetterRatioInURL`**: Доля букв в URL.
- **`NoOfDegitsInURL`**: Количество цифр в URL.
- **`DegitRatioInURL`**: Доля цифр в URL.
- **`NoOfEqualsInURL`**: Количество символов `=` в URL.
- **`NoOfQMarkInURL`**: Количество символов `?` в URL.
- **`NoOfAmpersandInURL`**: Количество символов `&` в URL.
- **`NoOfOtherSpecialCharsInURL`**: Количество других специальных символов в URL.
- **`SpacialCharRatioInURL`**: Доля специальных символов в URL.

### Безопасность
- **`IsHTTPS`**: Использует ли URL HTTPS (0 — нет, 1 — да).

### Содержимое страницы
- **`LineOfCode`**: Количество строк кода на странице.
- **`LargestLineLength`**: Длина самой длинной строки кода.
- **`HasTitle`**: Флаг наличия тега `<title>`.
- **`Title`**: Заголовок страницы.
- **`DomainTitleMatchScore`**: Индекс совпадения заголовка с доменом.
- **`URLTitleMatchScore`**: Индекс совпадения заголовка с URL.

### Дополнительные признаки
- **`HasFavicon`**: Наличие фавикона.
- **`Robots`**: Присутствие файла `robots.txt`.
- **`IsResponsive`**: Является ли страница адаптивной.
- **`NoOfURLRedirect`**: Количество редиректов URL.
- **`NoOfSelfRedirect`**: Количество внутренних редиректов.

### Элементы страницы
- **`HasDescription`**: Наличие описания в метатеге.
- **`NoOfPopup`**: Количество всплывающих окон.
- **`NoOfiFrame`**: Количество `<iframe>` на странице.
- **`HasExternalFormSubmit`**: Флаг наличия формы с внешней отправкой.
- **`HasSocialNet`**: Наличие ссылок на социальные сети.
- **`HasSubmitButton`**: Наличие кнопки отправки.
- **`HasHiddenFields`**: Наличие скрытых полей.
- **`HasPasswordField`**: Наличие поля ввода пароля.

### Ключевые слова
- **`Bank`**: Наличие ключевого слова, связанного с банками.
- **`Pay`**: Наличие ключевого слова, связанного с платежами.
- **`Crypto`**: Наличие ключевого слова, связанного с криптовалютой.

### Прочие признаки
- **`HasCopyrightInfo`**: Наличие информации об авторских правах.
- **`NoOfImage`**: Количество изображений на странице.
- **`NoOfCSS`**: Количество подключенных CSS-файлов.
- **`NoOfJS`**: Количество подключенных JavaScript-файлов.
- **`NoOfSelfRef`**: Количество внутренних ссылок.
- **`NoOfEmptyRef`**: Количество пустых ссылок.
- **`NoOfExternalRef`**: Количество внешних ссылок.

### Метка
- **`label`**: Метка класса (1 — легитимный URL, 0 — фишинговый URL).

---