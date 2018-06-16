class Page():
    def __init__(self, page_num, total_count, url_prefix, per_page=10, max_page=11):
        """
        分页显示模块
        :param page_num:当前页码
        :param total_count: 对象总数
        :param url_prefix: 路由指向
        :param per_page: 每页显示多少条数据
        :param max_page: 最多页码
        """
        self.url_prefix = url_prefix
        self.max_page = max_page

        # calculate page number
        total_page, m = divmod(total_count, per_page)
        if m: total_page += 1
        self.total_page = total_page
        try:
            page_num = int(page_num)
            if page_num > total_page: page_num = total_page
        except Exception as e:
            page_num = 1
        self.page_num = page_num

        self.data_start = (page_num - 1) * 10
        self.data_end = page_num * 10

        # if total_page <= max_page or page_num < max_page // 2:
        #     page_start=0
        #     page_end=max_page
        # else:
        #     half_max_page = max_page // 2
        #     page_start = page_num - half_max_page
        #     page_end = page_num + half_max_page

        if total_page < self.max_page:
            self.max_page = total_page
        half_max_page = self.max_page // 2
        page_start = page_num - half_max_page
        page_end = page_num + half_max_page

        if page_start <= 1:
            page_start = 1
            page_end = self.max_page

        if page_end > total_page:
            page_end = total_page
            page_start = total_page - self.max_page + 1

        self.page_start = page_start
        self.page_end = page_end
        # all_person = models.Person.objects.all()[data_start:data_end]

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end

    def page_html(self):
        # concat html seperate code
        html_list = []
        html_list.append('<li><a href="{}?page=1">首页</a></li>'.format(self.url_prefix))
        if self.page_num <= 1:
            html_list.append(
                '<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
        else:
            html_list.append(
                '<li><a href="{}?page={}" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>'.format(
                    self.page_num - 1, self.url_prefix))

        for i in range(self.page_start, self.page_end + 1):
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            html_list.append(tmp)

        if self.page_num >= self.total_page:
            html_list.append(
                '<li class="disabled"><a href="#" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_list.append(
                '<li><a href="{0}?page={1}" aria-label="Next"><span aria-hidden="true">&raquo;</span></a></li>'.format(
                    self.url_prefix, self.page_num + 1))

        html_list.append('<li><a href="{}?page={}">尾页</a></li>'.format(self.url_prefix, self.total_page))
        page_html = "".join(html_list)
        return page_html
