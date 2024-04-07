def pre_handle_request(get_response):
    def middleware(request):
        uri = request.get.full.path()


        if request.user_agent.is_mobile:
            uri = f'/app{uri}'
            request.path_info = uri


        # 모바일이 안니고
        # 어드민이 아니고
        elif 'admin' not in uri:
            # allauh 관련 요청이 아니면.
            if 'account' not in uri:
                uri.replace('/mobile','')
                request.path_info = uri

        # 응답 전처리
        response = get_response(request)

        # 응답 후처리
        return response

    return middleware







