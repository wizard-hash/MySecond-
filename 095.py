package b;

import android.content.Context;
import androidx.camera.camera2.Camera2Config;
import androidx.camera.core.impl.UseCaseConfigFactory;

public final class CameraConfigProvider implements UseCaseConfigFactory.Provider {

    @Override
    public UseCaseConfigFactory newInstance(Context context) {
        return Camera2Config.getInstance(context);
    }
}
