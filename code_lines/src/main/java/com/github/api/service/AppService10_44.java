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
 * @date 2020/12/30 10:32:09
 * <p>
 * Email: liyongwang@yiche.com
 */
public interface AppService10_44 {
    /**
    * /user/hasawardqualified 7 薛文强 2020-12-25 17:35:26 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4076&enterType=1&projectID=1
    * @param userId int 
    * @return
    */
    @GET(AppUrls10_44.USERCAR_SVC_USER_HASAWARDQUALIFIED)
    Observable<HttpResult<Object>> usercar_svc_user_hasawardqualified(@Query("userId") @NonNull int userId);

    /**
    * 修改子任务状态 6 谢鹏 2020-12-24 19:55:11 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4069&enterType=1&projectID=1
    * @param id int 
    * @param status int 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_44.WEB_V1_SON_TASK_MODIFY_STATUS)
    Observable<HttpResult<Object>> web_v1_son_task_modify_status(@Field("id")  int id, @Field("status")  int status);

    /**
    * 查询子任务详情 6 谢鹏 2020-12-24 19:52:54 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4067&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.WEB_V1_SON_TASK_DETAIL)
    Observable<HttpResult<Object>> web_v1_son_task_detail(@Query("param") @NonNull String param);

    /**
    * 查询子任务列表 6 谢鹏 2020-12-24 19:51:56 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4066&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.AWARD_TASK_WEB_WEB_V1_SON_TASK_LIST)
    Observable<HttpResult<Object>> award_task_web_web_v1_son_task_list(@Query("param") @NonNull String param);

    /**
    * 线索相关猜你喜欢 6 魏明勋 2020-12-23 19:29:17 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4055&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.APPUCAR_APP_DEALER_API_V1_GUESS_GUESSYOULIKE)
    Observable<HttpResult<Object>> appucar_app_dealer_api_v1_guess_guessYouLike(@Query("param") @NonNull String param);

    /**
    * 商业车型(同级车)查询经销商列表 6 魏明勋 2020-12-24 17:13:05 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4054&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.API_V1_ENQUIRY_GETENQUIRYBUSINESSVEHICLEMODELDEALERLIST)
    Observable<HttpResult<Object>> api_v1_enquiry_getEnquiryBusinessVehicleModelDealerList(@Query("param") @NonNull String param);

    /**
    * 商业车型(同级车)查询询价详情 6 张连敏 2020-12-23 20:08:25 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4053&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.API_V1_ENQUIRY_GETENQUIRYINFOFORBUSINESSVEHICLEMODEL)
    Observable<HttpResult<Object>> api_v1_enquiry_getEnquiryInfoForBusinessVehicleModel(@Query("param") @NonNull String param);

    /**
    * 根据carIds获取分组下所有车款(查车型库) 1   http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4047&enterType=1&projectID=1
    * @param carIds String 车款id，逗号分隔
    * @param app_ver String 版本号
    * @return
    */
    @GET(AppUrls10_44.CARDIFFAPPAPI_CARDIFF_API_WISHCONFIGLIST_GETCARBYCARIDS)
    Observable<HttpResult<Object>> cardiffappapi_cardiff_api_wishconfiglist_getcarbycarids(@Query("carIds") @NonNull String carIds, @Query("app_ver") @NonNull String app_ver);

    /**
    * 根据车型查询分组与对应最后车款的参配（查车型库） 1   http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4045&enterType=1&projectID=1
    * @param serialId int 车系id
    * @param app_ver String 版本号
    * @return
    */
    @GET(AppUrls10_44.CARDIFFAPPAPI_CARDIFF_API_WISHCONFIGLIST_GETGROUPANDCARPARAMLISTV2)
    Observable<HttpResult<Object>> cardiffappapi_cardiff_api_wishconfiglist_getgroupandcarparamlistv2(@Query("serialId") @NonNull int serialId, @Query("app_ver") @NonNull String app_ver);

    /**
    * 用户任务信息列表 6 王刘风 2020-12-24 12:04:09 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4038&enterType=1&projectID=1
    * @return
    */
    @GET(AppUrls10_44.WEB_API_AWARD_TASK_API_API_V1_USER_TASK_USER_TASK_LIST)
    Observable<HttpResult<Object>> web_api_award_task_api_api_v1_user_task_user_task_list();

    /**
    * admin根据regionId删除城市信息 7   http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4037&enterType=1&projectID=1
    * @param regionId int 统计局城市id
    * @return
    */
    @GET(AppUrls10_44.CITYBASE_ADMIN_CITY_DELETECITYBYREGIONID)
    Observable<HttpResult<Object>> citybase_admin_city_deleteCityByRegionId(@Query("regionId") @NonNull int regionId);

    /**
    * 是否弹出用户隐私信息授权弹窗 6   http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4027&enterType=1&projectID=1
    * @return
    */
    @GET(AppUrls10_44.API_BENEFIT_APP_V1_OIL_AUTHORIZE_POPUP)
    Observable<HttpResult<Object>> api_benefit_app_v1_oil_authorize_popup();

    /**
    * 同级车接口 6   http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4024&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.APP_CARMODEL_API_V1_CARMODEL_GET_COMPETITOR_LIST)
    Observable<HttpResult<Object>> app_carmodel_api_v1_carmodel_get_competitor_list(@Query("param") @NonNull String param);

    /**
    * 执行(完成任务) 6 陈进军 2020-12-23 15:26:56 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4022&enterType=1&projectID=1
    * @param classifyCode String 
    * @param businessData String 
    * @param progressData int 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_44.AWARD_TASK_API_API_V1_USER_TASK_COMPLETE_TASK)
    Observable<HttpResult<Object>> award_task_api_api_v1_user_task_complete_task(@Field("classifyCode")  String classifyCode, @Field("businessData")  String businessData, @Field("progressData")  int progressData);

    /**
    * 个人中心-为你推荐 6 赵军凯 2020-12-22 20:05:24 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4021&enterType=1&projectID=1
    * @param param String {"pageNo":1}
    * @param cid String 200
    * @param ver String 10.44
    * @return
    */
    @GET(AppUrls10_44.APP_USER_API_V1_RECOMMEND_RECOMMEND_INFO)
    Observable<HttpResult<Object>> app_user_api_v1_recommend_recommend_info(@Query("param") @NonNull String param, @Query("cid") @NonNull String cid, @Query("ver") @NonNull String ver);

    /**
    * 直播推荐tab直播列表 6 张文凯 2020-12-22 17:18:16 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4019&enterType=1&projectID=1
    * @param param String 
    * @return
    */
    @GET(AppUrls10_44.APP_VIDEO_API_V1_LIVE_LIVE_TAB_LIVE_LIST)
    Observable<HttpResult<Object>> app_video_api_v1_live_live_tab_live_list(@Query("param") @NonNull String param);

    /**
    * 直播回放数据获取：取近1个月的类别为选车、新车、活动、车展、试驾评测、说车、直播答题的7种类别的直播回放，按照时间倒叙排列展示在推荐信息流 7 孟德坤 2020-12-22 15:10:52 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=4009&enterType=1&projectID=1
    * @param pageNum int 页码
    * @param pageSize int 页条数
    * @return
    */
    @GET(AppUrls10_44.LIVEAPP_LIVE_GETBACKLISTLASTMONTH)
    Observable<HttpResult<Object>> liveapp_live_getBackListLastMonth(@Query("pageNum") @NonNull int pageNum, @Query("pageSize") @NonNull int pageSize);

    /**
    * 获取是否显示定制心愿配置 6 李峰（应用研发部） 2020-12-22 16:52:01 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=3353&enterType=1&projectID=1
    * @param param String 车款id(车款页需要传)
    * @return
    */
    @GET(AppUrls10_44.APP_CARMODEL_API_V1_CARMODEL_GET_IF_SHOW_CUSTOM_CONFIG)
    Observable<HttpResult<Object>> app_carmodel_api_v1_carmodel_get_if_show_custom_config(@Query("param") @NonNull String param);

    /**
    * 获取回复列表接口 7 尹力（用户资讯部） 2020-12-23 10:18:38 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=1703&enterType=1&projectID=1
    * @param topId String 评论ID
    * @param productId String 业务线ID
    * @param objectId String 评论对象ID
    * @param pageSize String 分页大小
    * @param pageIndex String 页码
    * @param isHot String list是否按热门排序
    * @return
    */
    @GET(AppUrls10_44.COMMENT_APP_GETREPLYLIST)
    Observable<HttpResult<Object>> comment_app_getreplylist(@Query("topId") @NonNull String topId, @Query("productId") @NonNull String productId, @Query("objectId") @NonNull String objectId, @Query("pageSize") @NonNull String pageSize, @Query("pageIndex") @NonNull String pageIndex, @Query("isHot") @NonNull String isHot);

    /**
    * 获取主评论列表接口 7 尹力（用户资讯部） 2020-12-23 10:18:11 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=1701&enterType=1&projectID=1
    * @param productId String 
    * @param pageIndx String 
    * @param pageSize String 
    * @param objectId String 
    * @param laseId String 
    * @param deviceId String 
    * @return
    */
    @GET(AppUrls10_44.COMMENT_APP_GETTOPLIST)
    Observable<HttpResult<Object>> comment_app_gettoplist(@Query("productId") @NonNull String productId, @Query("pageIndx") @NonNull String pageIndx, @Query("pageSize") @NonNull String pageSize, @Query("objectId") @NonNull String objectId, @Query("laseId") @NonNull String laseId, @Query("deviceId") @NonNull String deviceId);

    /**
    * 管理车辆分组-分组列表 1 王磊(车型研发部) 2020-12-23 15:50:00 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=1265&enterType=1&projectID=1
    * @param serialId int 车系id
    * @param year int 年款
    * @return
    */
    @GET(AppUrls10_44.CAR_OP_DIFF_MANAGER_GETGROUPLIST)
    Observable<HttpResult<Object>> car_op_diff_manager_getGroupList(@Query("serialId") @NonNull int serialId, @Query("year") @NonNull int year);

    /**
    * 管理车辆分组-新增分组 1 王磊(车型研发部) 2020-12-23 15:48:53 http://192.168.87.178:8001/#/port/checkPortInfo?apiID=1231&enterType=1&projectID=1
    * @param groupName String 
    * @param serialId int 
    * @param year int 
    * @param selectGroupName String 
    * @return
    */
    @FormUrlEncoded
    @POST(AppUrls10_44.CAR_OP_DIFF_MANAGER_ADDGROUP)
    Observable<HttpResult<Object>> car_op_diff_manager_addGroup(@Field("groupName")  String groupName, @Field("serialId")  int serialId, @Field("year")  int year, @Field("selectGroupName")  String selectGroupName);


}