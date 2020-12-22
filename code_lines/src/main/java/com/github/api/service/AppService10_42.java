package com.github.api.service;

import com.bitauto.libcommon.net.model.HttpResult;
import retrofit2.http.Multipart;
import okhttp3.MultipartBody;
import io.reactivex.Observable;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.POST;
import android.support.annotation.NonNull;
import retrofit2.http.Query;

/**
 * @author Lyongwang
 * @date 2020/12/09 14:10:25
 * <p>
 * Email: liyongwang@yiche.com
 */
public interface AppService10_42 {
    /**
    * 综述页点评列表 6 谭向国 2020-11-24 17:50:48
    * @param param String 车系id
    * @return
    */
    @GET(AppUrls10_42.APP_REVIEW_API_V1_REVIEW_OVERVIEW_REVIEW_LIST_)
    Observable<HttpResult<Object>> app_review_api_v1_review_overview_review_list_(@Query("param") @NonNull String param);


}