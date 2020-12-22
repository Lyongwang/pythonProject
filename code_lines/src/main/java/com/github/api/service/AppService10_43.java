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
 * @date 2020/12/18 17:41:45
 * <p>
 * Email: liyongwang@yiche.com
 */
public interface AppService10_43 {
    /**
    * 车系基本信息v2 1  
    * @param serialId int 车系id
    * @param app_ver String 版本号
    * @return
    */
    @GET(AppUrls10_43.CAR_API_CARSERIALSUMMARY_V2_GETCARSERIALBASEINFO)
    Observable<HttpResult<Object>> car_api_carserialsummary_v2_getcarserialbaseinfo(@Query("serialId") @NonNull int serialId, @Query("app_ver") @NonNull String app_ver);

    /**
    * 车系基本信息 1 何英彬 2020-12-09 00:11:28
    * @param serialId int 车系id
    * @param app_ver String 版本号
    * @return
    */
    @GET(AppUrls10_43.CAR_API_CARSERIALSUMMARY_GETCARSERIALBASEINFO)
    Observable<HttpResult<Object>> car_api_carserialsummary_getCarSerialBaseInfo(@Query("serialId") @NonNull int serialId, @Query("app_ver") @NonNull String app_ver);

    /**
    * 清理分组名称的发动机的功率为马力（电动车不处理） 1  
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.CAR_OP_DIFF_CLEANDATA_GROUPNAME)
    Observable<HttpResult<Object>> car_op_diff_cleandata_groupname();

    /**
    * 综述页猜你喜欢 6  
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APPUCAR_APP_MOTO_API_V1_MOTO_GET_LIKE_SERIALS)
    Observable<HttpResult<Object>> appucar_app_moto_api_v1_moto_get_like_serials(@Query("param") @NonNull String param);

    /**
    * 综述页车款列表 6 秦世飞 2020-12-09 15:05:10
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APPUCAR_APP_MOTO_API_V1_MOTO_GET_CAR_LIST)
    Observable<HttpResult<Object>> appucar_app_moto_api_v1_moto_get_car_list(@Query("param") @NonNull String param);

    /**
    * 摩托车综述页头部 6  
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APPUCAR_APP_MOTO_API_V1_MOTO_GET_SUMMARY_HEAD)
    Observable<HttpResult<Object>> appucar_app_moto_api_v1_moto_get_summary_head(@Query("param") @NonNull String param);

    /**
    * 个人中心腰部banner V2 接口 6  
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.USER_CENTER_USER_BANNER_V2)
    Observable<HttpResult<Object>> user_center_user_banner_v2();

    /**
    * 推荐操作 1  
    * @param id int ID
    * @param recommendType int 推荐类别	
    * @param operUserId int 操作人id	
    * @param operUserName String 操作人名称	
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.ADMIN_RECOMMEND)
    Observable<HttpResult<Object>> admin_recommend(@Field("id") @NonNull int id, @Field("recommendType") @NonNull int recommendType, @Field("operUserId") @NonNull int operUserId, @Field("operUserName") @NonNull String operUserName);

    /**
    * 查询摩托车主品牌列表 0 谢鹏 2020-12-07 15:14:33
    * @return
    */
    @GET(AppUrls10_43.WEB_MP_API_V1_PUB_MOTOR_MASTER)
    Observable<HttpResult<Object>> web_mp_api_v1_pub_motor_master();

    /**
    * TD拉活 6 魏明勋 2020-12-04 11:25:12
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.API_V1_ACTIVATION_REPORTDATA)
    Observable<HttpResult<Object>> api_v1_activation_reportData(@Query("param")  String param);

    /**
    * 保存评论（对外） 7 袁军涛 2020-12-08 15:18:56
    * @param productId int 业务线
    * @param objectId String 对象ID
    * @param parentId Long 父ID
    * @param tuserId int 易湃用户ID
    * @param content String 内容
    * @param client int 客户端
    * @param source int 来源
    * @param channelNo int 渠道号 1易车 2易湃 3报价
    * @param sign String 签名
    * @param deviceId String 设备号
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.COMMENT_OUT_APP_SAVE)
    Observable<HttpResult<Object>> comment_out_app_save(@Field("productId") @NonNull int productId, @Field("objectId") @NonNull String objectId, @Field("parentId") @NonNull Long parentId, @Field("tuserId") @NonNull int tuserId, @Field("content") @NonNull String content, @Field("client") @NonNull int client, @Field("source") @NonNull int source, @Field("channelNo") @NonNull int channelNo, @Field("sign") @NonNull String sign, @Field("deviceId")  String deviceId);

    /**
    * 获取线索按钮 6 魏明勋 2020-12-08 13:54:08
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.API_V1_GET_CLUE_BUTTON)
    Observable<HttpResult<Object>> api_v1_get_clue_button(@Query("param")  String param);

    /**
    * 获取摩托车参数配置 6 李峰（应用研发部） 2020-12-07 16:38:23
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APPUCAR_APP_MOTO_API_V1_MOTO_GET_PARAM_CONFIG)
    Observable<HttpResult<Object>> appucar_app_moto_api_v1_moto_get_param_config(@Query("param") @NonNull String param);

    /**
    * 咨询-关联车型新 6 李峰（应用研发部） 2020-12-07 16:31:58
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APPUCAR_APP_DEALER_API_V1_CAR_GET_RELATE_SERIAL_V2)
    Observable<HttpResult<Object>> appucar_app_dealer_api_v1_car_get_relate_serial_v2(@Query("param") @NonNull String param);

    /**
    * 获取零回复主贴列表 7 肖建宇 2020-12-08 16:11:01
    * @param postType int 帖子类型
    * @param pageIndex int 页码，默认值1，最大50限制
    * @param pageSize int 每页条数，默认值20，最大50限制
    * @return
    */
    @GET(AppUrls10_43.YICHEFORUM_SVC_APPAPI_TOPIC_GETZEROREPLYTOPICLIST)
    Observable<HttpResult<Object>> yicheforum_svc_appapi_topic_getzeroreplytopiclist(@Query("postType") @NonNull int postType, @Query("pageIndex") @NonNull int pageIndex, @Query("pageSize") @NonNull int pageSize);

    /**
    * 详情页更多点评列表 6 谭向国 2020-12-04 17:28:48
    * @param param String 车系id
    * @return
    */
    @GET(AppUrls10_43.APP_REVIEW_API_V1_REVIEW_GET_MORE)
    Observable<HttpResult<Object>> app_review_api_v1_review_get_more(@Query("param") @NonNull String param);

    /**
    * 弃用，不要点 6 董越 2020-12-04 11:14:53
    * @return
    */
    @GET(AppUrls10_43.XXXXXXXXXXXX)
    Observable<HttpResult<Object>> xxxxxxxxxxxx();

    /**
    * 小视频后台审核批量审核通过 7 刘春洪 2020-12-07 10:16:54
    * @param videoIds String 小视频id
    * @param auditState int 审核状态
    * @param messageId String 
    * @param content String 
    * @param msgType String 
    * @param isHighQuality String 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.PROVIDER_VIDEO_ADMIN_CLOUD_VIDEO_ADMIN_BATCHAUDIT)
    Observable<HttpResult<Object>> provider_video_admin_cloud_video_admin_batchaudit(@Field("videoIds") @NonNull String videoIds, @Field("auditState") @NonNull int auditState, @Field("messageId") @NonNull String messageId, @Field("content") @NonNull String content, @Field("msgType") @NonNull String msgType, @Field("isHighQuality") @NonNull String isHighQuality);

    /**
    * 修改选配包 1 王磊(车型研发部) 2020-12-09 11:52:39
    * @param year String 
    * @param price int 
    * @param packageId int 
    * @param name String 
    * @param description String 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.CARMOTO_CAR_OP_MOTO_PACKAGE_UPDATE)
    Observable<HttpResult<Object>> carmoto_car_op_moto_package_update(@Field("year")  String year, @Field("price")  int price, @Field("packageId")  int packageId, @Field("name")  String name, @Field("description")  String description);

    /**
    * 新增选配包 1 王磊(车型研发部) 2020-12-03 17:36:43
    * @param serialId int 
    * @param price int 
    * @param name String 
    * @param description String 
    * @param years String 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_43.CARMOTO_CAR_OP_MOTO_PACKAGE_ADD)
    Observable<HttpResult<Object>> carmoto_car_op_moto_package_add(@Field("serialId")  int serialId, @Field("price")  int price, @Field("name")  String name, @Field("description")  String description, @Field("years")  String years);

    /**
    * 活动 6 张连敏 2020-12-09 16:03:58
    * @param param String 
    * @param reqid String 
    * @param a String 
    * @return
    */
    @GET(AppUrls10_43.APP_THIRD_API_V1_PACKAGE_GET_ACTIVE)
    Observable<HttpResult<Object>> app_third_api_v1_package_get_active(@Query("param") @NonNull String param, @Query("reqid") @NonNull String reqid, @Query("a") @NonNull String a);

    /**
    * APP-回帖列表 6 董越 2020-12-03 16:43:07
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APP_FORUM_API_REPLY_GETLIST)
    Observable<HttpResult<Object>> app_forum_api_reply_getlist(@Query("param") @NonNull String param);

    /**
    * 10、获取车型下的问题列表，带一个回答 7 刘春洪 2020-12-09 16:19:49
    * @param masterid String 品牌id
    * @param serialid String 车系id
    * @param carid String 车款id
    * @param ordertype String 排序（0：默认，1最新）
    * @param tag String 标签id
    * @param taglevel String 标签级别
    * @param isunsolved String 是否是未解决（0：全部，1：未解决）
    * @param pageindex String 当前分页
    * @param pagesize String 每页条数
    * @param app_key String 网关参数
    * @return
    */
    @GET(AppUrls10_43.ASK_SVC_QUESTION_GETQUESTIONLISTBYCAR)
    Observable<HttpResult<Object>> ask_svc_question_getquestionlistbycar(@Query("masterid") @NonNull String masterid, @Query("serialid") @NonNull String serialid, @Query("carid") @NonNull String carid, @Query("ordertype") @NonNull String ordertype, @Query("tag") @NonNull String tag, @Query("taglevel") @NonNull String taglevel, @Query("isunsolved") @NonNull String isunsolved, @Query("pageindex") @NonNull String pageindex, @Query("pagesize") @NonNull String pagesize, @Query("app_key") @NonNull String app_key);

    /**
    * 首页-小视频列表小视频推荐列表接口 6 张文凯 2020-12-04 17:34:02
    * @param param String 
    * @return
    */
    @GET(AppUrls10_43.APP_VIDEO_API_V1_VIDEO_SMALL_GET_RECOMMENT_APPLIST)
    Observable<HttpResult<Object>> app_video_api_v1_video_small_get_recomment_applist(@Query("param") @NonNull String param);


}