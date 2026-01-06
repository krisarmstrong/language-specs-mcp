# XRView

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

- [Learn more](/en-US/docs/Glossary/Baseline/Compatibility)
- [See full compatibility](#browser_compatibility)
- [Report feedback](https://survey.alchemer.com/s3/7634825/MDN-baseline-feedback?page=%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRView&level=not)

Secure context: This feature is available only in [secure contexts](/en-US/docs/Web/Security/Defenses/Secure_Contexts) (HTTPS), in some or all [supporting browsers](#browser_compatibility).

Experimental:This is an [experimental technology](/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
Check the [Browser compatibility table](#browser_compatibility) carefully before using this in production.

The [WebXR Device API](/en-US/docs/Web/API/WebXR_Device_API)'s `XRView` interface describes a single view into the XR scene for a specific frame, providing orientation and position information for the viewpoint. You can think of it as a description of a specific eye or camera and how it views the world. A 3D frame will involve two views, one for each eye, separated by an appropriate distance which approximates the distance between the viewer's eyes. This allows the two views, when projected in isolation into the appropriate eyes, to simulate a 3D world.

## In this article

- [Instance properties](#instance_properties)
- [Instance methods](#instance_methods)
- [Usage notes](#usage_notes)
- [Examples](#examples)
- [Specifications](#specifications)
- [Browser compatibility](#browser_compatibility)

## [Instance properties](#instance_properties)

[eye](/en-US/docs/Web/API/XRView/eye)Read onlyExperimental

Which of the two eyes (`left`) or (`right`) for which this `XRView` represents the perspective. This value is used to ensure that any content which is pre-rendered for presenting to a specific eye is distributed or positioned correctly. The value can also be `none` if the `XRView` is presenting monoscopic data (such as a 2D image, a fullscreen view of text, or a close-up view of something that doesn't need to appear in 3D).

[isFirstPersonObserver](/en-US/docs/Web/API/XRView/isFirstPersonObserver)Read onlyExperimental

Returns a boolean indicating if the `XRView` is a first-person observer view.

[projectionMatrix](/en-US/docs/Web/API/XRView/projectionMatrix)Read onlyExperimental

The projection matrix that will transform the scene to appear correctly given the point-of-view indicated by `eye`. This matrix should be used directly in order to avoid presentation distortions that may lead to potentially serious user discomfort.

[recommendedViewportScale](/en-US/docs/Web/API/XRView/recommendedViewportScale)Read onlyExperimental

The recommended viewport scale value that you can use for `requestViewportScale()` if the user agent has such a recommendation; [null](/en-US/docs/Web/JavaScript/Reference/Operators/null) otherwise.

[transform](/en-US/docs/Web/API/XRView/transform)Read onlyExperimental

An [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform) which describes the current position and orientation of the viewpoint in relation to the [XRReferenceSpace](/en-US/docs/Web/API/XRReferenceSpace) specified when [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) was called on the [XRFrame](/en-US/docs/Web/API/XRFrame) being rendered.

## [Instance methods](#instance_methods)

[requestViewportScale()](/en-US/docs/Web/API/XRView/requestViewportScale)Read onlyExperimental

Requests that the user agent should set the requested viewport scale for this viewport to the requested value.

## [Usage notes](#usage_notes)

### [Positions and number of XRViews per frame](#positions_and_number_of_xrviews_per_frame)

While rendering a scene, the set of views that are used to render the scene for the viewer as of the current frame are obtained by calling the [XRFrame](/en-US/docs/Web/API/XRFrame) object's [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose) method to get the [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) representing (in essence) the position of the viewer's head. That object's [views](/en-US/docs/Web/API/XRViewerPose/views) property is a list of all of the `XRView` objects representing the viewpoints which can be used to construct the scene for presentation to the user.

It's possible to have `XRView` objects which represent overlapping regions as well as entirely disparate regions; in a game, you might have views that can be presented to observe a remote site using a security camera or other device, for example. In other words, don't assume there are exactly two views on a given viewer; there can be as few as one (such as when rendering the scene in `inline` mode, and potentially many (especially if the field of view is very large). There might also be views representing observers watching the action, or other viewpoints not directly associated with a player's eye.

In addition, the number of views can change at any time, depending on the needs of the time. So you should process the view list every time without making assumptions based on previous frames.

All positions and orientations within the views for a given [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) are specified in the reference space that was passed to [XRFrame.getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose); this is called the viewer reference space. The [transform](/en-US/docs/Web/API/XRView/transform) property describes the position and orientation of the eye or camera represented by the `XRView`, given in that reference space.

### [The destination rendering layer](#the_destination_rendering_layer)

To render a frame, you iterate over the `XRViewerPose`'s views, rendering each of them into the appropriate viewport within the frame's [XRWebGLLayer](/en-US/docs/Web/API/XRWebGLLayer). Currently, the specification (and therefore all current implementations of WebXR) is designed around rendering every `XRView` into a single `XRWebGLLayer`, which is then presented on the XR device with half used for the left eye and half for the right eye. The [XRViewport](/en-US/docs/Web/API/XRViewport) for each view is used to position the rendering into the correct half of the layer.

If in the future it becomes possible for each view to render into a different layer, there would have to be changes made to the API, so it's safe for now to assume that all views will render into the same layer.

## [Examples](#examples)

### [Preparing to render every view for a pose](#preparing_to_render_every_view_for_a_pose)

To draw everything the user sees, each frame requires iterating over the list of views returned by the [XRViewerPose](/en-US/docs/Web/API/XRViewerPose) object's [views](/en-US/docs/Web/API/XRViewerPose/views) list:

js

```
for (const view of pose.views) {
  const viewport = glLayer.getViewport(view);

  gl.viewport(viewport.x, viewport.y, viewport.width, viewport.height);

  // Draw the scene; the eye being drawn is identified
  // by view.eye.
}
```

### [Special view transforms](#special_view_transforms)

There are a few special transforms that are used on the view while rendering and lighting a scene.

#### Model view matrix

The model view matrix is a matrix which defines the position of an object relative to the space in which it's located: If `objectMatrix` is a transform applied to the object to provide its basic position and rotation, then the model view matrix can be computed by multiplying the object's matrix by the inverse of the view transform matrix, like this:

js

```
mat4.multiply(modelViewMatrix, view.transform.inverse.matrix, objectMatrix);
```

#### Normal matrix

The model view's normal matrix is used when lighting the scene, in order to transform each surface's normal vectors to ensure that the light is reflected in the correct direction given the orientation and position of the surface relative to the light source or sources. It's computed by inverting then transposing the model view matrix:

js

```
mat4.invert(normalMatrix, modelViewMatrix);
mat4.transpose(normalMatrix, normalMatrix);
```

### [Teleporting an object](#teleporting_an_object)

To programmatically move and/or rotate (often referred to as teleporting) an object, you need to create a new reference space for that object which applies a transform that encapsulates the desired changes. The `createTeleportTransform()` function returns the transform needed to move and rotate an object whose current situation is described by the reference space `refSpace` to a new position and orientation which is computed using previously recorded mouse and keyboard input data which has generated offsets for yaw, pitch, and position along all three axes.

js

```
function applyMouseMovement(refSpace) {
  if (
    !mouseYaw &&
    !mousePitch &&
    !axialDistance &&
    !transverseDistance &&
    !verticalDistance
  ) {
    return refSpace;
  }

  // Compute the quaternion used to rotate the image based
  // on the pitch and yaw.

  quat.identity(inverseOrientation);
  quat.rotateX(inverseOrientation, inverseOrientation, -mousePitch);
  quat.rotateY(inverseOrientation, inverseOrientation, -mouseYaw);

  // Compute the true "up" vector for our object.

  vec3.cross(vecX, vecY, cubeOrientation);
  vec3.cross(vecY, cubeOrientation, vecX);

  // Now compute the transform that teleports the object to the
  // specified point and save a copy of it to display to the user
  // later; otherwise we probably wouldn't need to save mouseMatrix
  // at all.

  let newTransform = new XRRigidTransform(
    { x: transverseDistance, y: verticalDistance, z: axialDistance },
    {
      x: inverseOrientation[0],
      y: inverseOrientation[1],
      z: inverseOrientation[2],
      w: inverseOrientation[3],
    },
  );
  mat4.copy(mouseMatrix, newTransform.matrix);

  // Create a new reference space that transforms the object to the new
  // position and orientation, returning the new reference space.

  return refSpace.getOffsetReferenceSpace(newTransform);
}
```

This code is broken into four sections. In the first, the quaternion `inverseOrientation` is computed. This represents the rotation of the object given the values of `mousePitch` (rotation around the object's reference's space's X axis) and `mouseYaw` (rotation around the object's Y axis).

The second section computes the "up" vector for the object. This vector indicates the direction which is "up" in the scene overall, but in the object's reference space.

The third section creates the new [XRRigidTransform](/en-US/docs/Web/API/XRRigidTransform), specifying a point providing the offsets along the three axes as the first parameter, and the orientation quaternion as the second parameter. The returned object's [matrix](/en-US/docs/Web/API/XRRigidTransform/matrix) property is the actual matrix that transforms points from the scene's reference space to the object's new position.

Finally, a new reference space is created to describe the relationship between the two reference spaces fully. That reference space is returned to the caller.

To use this function, we pass the returned reference space into [XRFrame.getPose()](/en-US/docs/Web/API/XRFrame/getPose) or [getViewerPose()](/en-US/docs/Web/API/XRFrame/getViewerPose), as appropriate for your needs. The returned [XRPose](/en-US/docs/Web/API/XRPose) will then be used to render the scene for the current frame.

You can find a more extensive and complete example in our article [Movement, orientation, and motion](/en-US/docs/Web/API/WebXR_Device_API/Movement_and_motion).

## [Specifications](#specifications)

Specification
[WebXR Device API# xrview-interface](https://immersive-web.github.io/webxr/#xrview-interface)

## [Browser compatibility](#browser_compatibility)

## Help improve MDN

Was this page helpful to you?YesNo[Learn how to contribute](/en-US/docs/MDN/Community/Getting_started)

 This page was last modified on ⁨Jul 7, 2023⁩ by [MDN contributors](/en-US/docs/Web/API/XRView/contributors.txt). 

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/api/xrview/index.md?plain=1) • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRView&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fapi%2Fxrview%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FXRView%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fapi%2Fxrview%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Facfe8c9f1f4145f77653a2bc64a9744b001358dc%0A*+Document+last+modified%3A+2023-07-07T07%3A19%3A19.000Z%0A%0A%3C%2Fdetails%3E)
