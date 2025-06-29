package hu.ekreta.ellenorzo.data.remote.idp;

import hu.ekreta.ellenorzo.data.remote.Authentication;
import hu.ekreta.ellenorzo.data.remote.idp.v1.AuthenticationDto;
import hu.ekreta.ellenorzo.data.remote.idp.v1.UserInfo;
import hu.ekreta.framework.core.data.AnalyticsEvent;
import hu.ekreta.framework.core.data.AnalyticsParam;
import io.opentelemetry.diskbuffering.proto.common.v1.AnyValue;
import io.reactivex.Observable;
import io.reactivex.Single;
import kotlin.Metadata;
import kotlin.coroutines.Continuation;
import kotlin.reflect.jvm.internal.impl.metadata.WE.XjihuAaNZ;
import kotlinx.coroutines.future.dqis.VolvpZjVtx;
import okhttp3.ResponseBody;
import retrofit2.http.Field;
import retrofit2.http.FormUrlEncoded;
import retrofit2.http.GET;
import retrofit2.http.Header;
import retrofit2.http.POST;

@Metadata(d1 = {"\u00008\n\u0002\u0018\u0002\n\u0002\u0010\u0000\n\u0000\n\u0002\u0018\u0002\n\u0000\n\u0002\u0010\u000e\n\u0002\b\u0004\n\u0002\u0010\u000b\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0006\n\u0002\u0018\u0002\n\u0002\u0018\u0002\n\u0002\b\u0002\bf\u0018\u00002\u00020\u0001JT\u0010\u0002\u001a\u00020\u00032\b\b\u0001\u0010\u0004\u001a\u00020\u00052\b\b\u0001\u0010\u0006\u001a\u00020\u00052\b\b\u0003\u0010\u0007\u001a\u00020\u00052\b\b\u0003\u0010\b\u001a\u00020\u00052\b\b\u0003\u0010\t\u001a\u00020\n2\b\b\u0003\u0010\u000b\u001a\u00020\u00052\b\b\u0003\u0010\f\u001a\u00020\u0005H§@¢\u0006\u0002\u0010\rJ\u000e\u0010\u000e\u001a\u00020\u0005H§@¢\u0006\u0002\u0010\u000fJ\u000e\u0010\u0010\u001a\b\u0012\u0004\u0012\u00020\u00120\u0011H'J^\u0010\u0013\u001a\u00020\u00032\b\b\u0001\u0010\u0014\u001a\u00020\u00052\b\b\u0001\u0010\u0015\u001a\u00020\u00052\b\b\u0001\u0010\u0006\u001a\u00020\u00052\b\b\u0003\u0010\u0007\u001a\u00020\u00052\b\b\u0003\u0010\b\u001a\u00020\u00052\b\b\u0003\u0010\u0016\u001a\u00020\u00052\b\b\u0003\u0010\u000b\u001a\u00020\u00052\b\b\u0003\u0010\f\u001a\u00020\u0005H§@¢\u0006\u0002\u0010\u0017J,\u0010\u0018\u001a\b\u0012\u0004\u0012\u00020\u001a0\u00192\b\b\u0001\u0010\u0004\u001a\u00020\u00052\b\b\u0003\u0010\b\u001a\u00020\u00052\b\b\u0003\u0010\u001b\u001a\u00020\u0005H'¨\u0006\u001c"}, d2 = {"Lhu/ekreta/ellenorzo/data/remote/idp/IdpApiV1;", AnyValue.DEFAULT_STRING_VALUE, "extendToken", "Lhu/ekreta/ellenorzo/data/remote/idp/v1/AuthenticationDto;", "refreshToken", AnyValue.DEFAULT_STRING_VALUE, AnalyticsParam.INSTITUTE_CODE, "grantType", "clientId", "refreshUserData", AnyValue.DEFAULT_STRING_VALUE, "authKey", "authVersion", "(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;ZLjava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "getNonce", "(Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "getUserInfo", "Lio/reactivex/Single;", "Lhu/ekreta/ellenorzo/data/remote/idp/v1/UserInfo;", AnalyticsEvent.ANALYTICS_LOGIN, "userName", "password", "authNonce", "(Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Ljava/lang/String;Lkotlin/coroutines/Continuation;)Ljava/lang/Object;", "revokeRefreshToken", "Lio/reactivex/Observable;", "Lokhttp3/ResponseBody;", "tokenType", "app_googleStudentProdRelease"}, k = 1, mv = {1, 9, 0}, xi = 48)
/* loaded from: C:\Users\vajkh\AppData\Local\Temp\tmptssshu2q\classes3.dex */
public interface IdpApiV1 {

    @Metadata(k = 3, mv = {1, 9, 0}, xi = 48)
    public static final class DefaultImpls {
        public static /* synthetic */ Object extendToken$default(IdpApiV1 idpApiV1, String str, String str2, String str3, String str4, boolean z2, String str5, String str6, Continuation continuation, int i, Object obj) {
            if (obj != null) {
                throw new UnsupportedOperationException("Super calls with default arguments not supported in this target, function: extendToken");
            }
            String str7 = (i & 4) != 0 ? "refresh_token" : str3;
            String str8 = (i & 8) != 0 ? "kreta-ellenorzo-mobile-android" : str4;
            boolean z3 = (i & 16) != 0 ? false : z2;
            int i2 = i & 32;
            String str9 = VolvpZjVtx.IgGOYhwLamAPs;
            return idpApiV1.extendToken(str, str2, str7, str8, z3, i2 != 0 ? str9 : str5, (i & 64) != 0 ? str9 : str6, continuation);
        }

        public static /* synthetic */ Object login$default(IdpApiV1 idpApiV1, String str, String str2, String str3, String str4, String str5, String str6, String str7, String str8, Continuation continuation, int i, Object obj) {
            if (obj == null) {
                return idpApiV1.login(str, str2, str3, (i & 8) != 0 ? "password" : str4, (i & 16) != 0 ? "kreta-ellenorzo-mobile-android" : str5, (i & 32) != 0 ? AnyValue.DEFAULT_STRING_VALUE : str6, (i & 64) != 0 ? AnyValue.DEFAULT_STRING_VALUE : str7, (i & 128) != 0 ? AnyValue.DEFAULT_STRING_VALUE : str8, continuation);
            }
            throw new UnsupportedOperationException(XjihuAaNZ.WRbCth);
        }

        public static /* synthetic */ Observable revokeRefreshToken$default(IdpApiV1 idpApiV1, String str, String str2, String str3, int i, Object obj) {
            if (obj != null) {
                throw new UnsupportedOperationException("Super calls with default arguments not supported in this target, function: revokeRefreshToken");
            }
            if ((i & 2) != 0) {
                str2 = "kreta-ellenorzo-mobile-android";
            }
            if ((i & 4) != 0) {
                str3 = "refresh token";
            }
            return idpApiV1.revokeRefreshToken(str, str2, str3);
        }
    }

    @FormUrlEncoded
    @POST("connect/token")
    Object extendToken(@Field("refresh_token") String str, @Field("institute_code") String str2, @Field("grant_type") String str3, @Field("client_id") String str4, @Field("refresh_user_data") boolean z2, @Header("X-AuthorizationPolicy-Key") String str5, @Header("X-AuthorizationPolicy-Version") String str6, Continuation<? super AuthenticationDto> continuation);

    @GET("nonce")
    Object getNonce(Continuation<? super String> continuation);

    @GET("connect/userinfo")
    @Authentication
    Single<UserInfo> getUserInfo();

    @FormUrlEncoded
    @POST("connect/token")
    Object login(@Field("userName") String str, @Field("password") String str2, @Field("institute_code") String str3, @Field("grant_type") String str4, @Field("client_id") String str5, @Header("X-AuthorizationPolicy-Nonce") String str6, @Header("X-AuthorizationPolicy-Key") String str7, @Header("X-AuthorizationPolicy-Version") String str8, Continuation<? super AuthenticationDto> continuation);

    @FormUrlEncoded
    @POST("connect/revocation")
    @Authentication
    Observable<ResponseBody> revokeRefreshToken(@Field("token") String refreshToken, @Field("client_id") String clientId, @Field("token_type") String tokenType);
}
