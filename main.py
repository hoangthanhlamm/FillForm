from configs.form import form
from services.autofill import AutoFill

if __name__ == '__main__':
    autofill = AutoFill(config=form)
    autofill.fill_contact_us({
        'name': 'Lam',
        'email': 'hoangthanhlamm@gmail.com',
        'message': 'Chúc ngon miệng!'
    })

    # urls = autofill.get_urls(n_responses=254)
    # with open('data/urls.txt', 'w', encoding='utf8') as f:
    #     # json.dump(urls, f, ensure_ascii=False)
    #     for url in urls:
    #         f.write(url)
    #         f.write('\n')


